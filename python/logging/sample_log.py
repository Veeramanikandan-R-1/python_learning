import os
import logging
logging.basicConfig(level=logging.DEBUG,filename='sample.log',filemode='a',format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
name='mani'

logger=logging.getLogger(__name__) #creating object

#create handler
w_handler=logging.StreamHandler()
e_handler=logging.FileHandler('file.log')
w_handler.setLevel(logging.WARNING)
e_handler.setLevel(logging.ERROR)

#creating formatters
c_format=logging.Formatter('%(name)s - %(levelName)s -%(message)s')
f_format=logging.Formatter('%(asctime)s %(name)s - %(levelName)s -%(message)s')
w_handler.setFormatter(c_format)

logger.debug('debug')
logger.info('{}\'s info'.format(name))
logger.warning('warning')
logger.error('error')
a,b=5,0
try:
	c=a/b
except Exception as e:
	logging.error('exception occured',exc_info=True)