
from datetime import datetime, timedelta

from utils.logging import logger


def write_to_db(email, password, digits_num, start_timestamp):
    logger.debug(email, password, digits_num, start_timestamp)


def read_from_db(code):
    mock_timestamp = 1650458261.042755

    start_time = datetime.fromtimestamp(float(mock_timestamp))

    if datetime.utcnow() - start_time > timedelta(minutes=1):
        return False

    return True
