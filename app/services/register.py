
from datetime import datetime

from services.db_service import write_to_db
from utils.logging import logger
from utils.number import get_4_digits


def register_service(email, password):
    digits_num = get_4_digits()
    now = datetime.utcnow()
    timestamp = datetime.timestamp(now)
    write_to_db(email, password, digits_num, timestamp)
    logger.info(f'4 digits code {digits_num} has been sent to {email}.')
    return {
        'status': 'OK',
        'message': f'4 digits code has been sent to your email {email}, please input in one minute.'
    }
