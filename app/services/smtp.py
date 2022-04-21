
from utils.logging import logger


def send_email_service(email, digits_num):
    logger.info(f'4 digits code {digits_num} has been sent to {email}.')
