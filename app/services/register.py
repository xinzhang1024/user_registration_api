
from datetime import datetime

from services.db_service import write_to_db
from utils.logging import logger
from utils.number import get_4_digits


def register_service(email, password):
    digits_num = get_4_digits()

    now = datetime.utcnow()
    timestamp = datetime.timestamp(now)

    try:
        write_to_db(email, password, digits_num, timestamp)
    except Exception as err:
        logger.debug(err)
        return False

    return True
