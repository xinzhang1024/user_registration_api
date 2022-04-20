
import logging
import os

LOGLEVEL = logging.INFO if os.getenv('env') == 'prod' else logging.DEBUG

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))

REGISTER_TAG = 'Register'
