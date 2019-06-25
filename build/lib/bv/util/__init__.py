__all__=['getCommonLogger','getLog4jLogger']
from . import logger as logger
from . import LoggerConfig as log4j
def getCommonLogger():
    return logger
def getLog4jLogger(name):
    logger = log4j.getLogger(name)
    
    return logger