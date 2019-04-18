from bv.algorithm.linearRegression import LinearRegression as ln

import logging
import bv.util.LoggerConfig as cfg
cfg.LogLevel=logging.DEBUG
##
##'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -  %(message)s', datefmt='%d-%b-%y %H:%M:%S')
lr = ln("linear regression","c:/traindata")

lr.toString()
logging.info("start work")
# ##
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# #