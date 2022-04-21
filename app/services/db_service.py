
from datetime import datetime, timedelta

import mysql.connector

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_DATABASE, DB_TABLE_NAME, EXPIRATION
from services.smtp import send_email_service
from utils.logging import logger


def table_exists(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(DB_TABLE_NAME.replace('\'', '\'\'')))
    if cursor.fetchone()[0] == 1:
        cursor.close()
        return True

    cursor.close()
    return False


def write_to_db(email, password, digits_num, start_timestamp):
    start_timestamp = str(start_timestamp)
    conn = None

    try:
        conn = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE
        )
        cursor = conn.cursor()
        if not table_exists(conn):
            cursor.execute(f'CREATE TABLE {DB_TABLE_NAME} (email VARCHAR(255) PRIMARY KEY, password VARCHAR(255), digits_num INT, start_timestamp VARCHAR(255))')

        insert_sql = f'INSERT INTO {DB_TABLE_NAME} (email, password, digits_num, start_timestamp) VALUES (%s, %s, %s, %s)'
        cursor.execute(insert_sql, (email, password, digits_num, start_timestamp))
        conn.commit()
        logger.info(f'Successfully write data {email}, {password}, {digits_num}, {start_timestamp} to db.')
        send_email_service(email, digits_num)
    except Exception as err:
        # ignore catch different errors.
        logger.debug(err)
        raise Exception('Failed to write data to db.')
    finally:
        conn.close()


def read_from_db(email, password):
    conn = None
    try:
        conn = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_DATABASE
        )
        cursor = conn.cursor()
        if not table_exists(conn):
            return False

        select_sql = f""" select * from {DB_TABLE_NAME} where email='{email}' """
        cursor.execute(select_sql)

        res = cursor.fetchall()

        if not len(res):
            return False

        db_email, db_password, db_code, db_timestamp = res[0]
        start_time = datetime.fromtimestamp(float(db_timestamp))

        if datetime.utcnow() - start_time > timedelta(minutes=EXPIRATION):
            logger.debug('time expired.')
            return False

        if db_password != password:
            logger.debug('password is not correct.')
            return False

        return str(db_code)
    except Exception as err:
        # ignore catch different errors.
        logger.debug(err)
        return False
    finally:
        conn.close()
