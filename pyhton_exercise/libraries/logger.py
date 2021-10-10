import logging
logging.basicConfig(filename="basic.log",format='%(asctime)s, %(message)s',filemode='w')
logger=logging.getLogger()

logger.setLevel(logging.INFO) #level below this will be ignored

logger.debug('harmless debug message')
logger.info('just an info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

