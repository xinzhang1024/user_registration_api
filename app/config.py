
import logging
import os

LOGLEVEL = logging.INFO if os.getenv('env') == 'prod' else logging.DEBUG

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))

REGISTER_TAG = 'Register'

DB_HOST = os.getenv('DB_SERVICE')
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
DB_PORT = os.getenv('MYSQL_PORT')
DB_DATABASE = os.getenv('MYSQL_DATABASE')
DB_TABLE_NAME = 'mysql_users'

EXPIRATION = 1
