# logging
import logging

import loggtest

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info('from main')

loggtest.do_something()