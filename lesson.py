# logging
import logging

# logging.basicConfig(filename='text.txt', level=logging.DEBUG)
formatter = '%(asctime)s:%(message)s'
# formatter = '%(levelname)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# logging.critical('critical') # default
# logging.error('error') # default
# logging.warning('warning') # default
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')