import logging
formatter = logging.Formatter('[%(asctime)s.%(msecs)03d ] (%(threadName)s) %(name)-12s %(levelname)-8s %(message)s', ' %Y-%m-%d %H:%M:%S',)
file_handler = logging.FileHandler("d:/trace.log")
file_handler.setFormatter(formatter)
LogLevel=logging.INFO
def config():
    global formatter
    global file_handler
    global LogLevel
    print("current log level:"+LogLevel)
def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LogLevel)
    logger.addHandler(file_handler)
    return logger
    
