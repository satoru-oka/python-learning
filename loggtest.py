import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('loggtest.log')
logger.addHandler(handler)

def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')