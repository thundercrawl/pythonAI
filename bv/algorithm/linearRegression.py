import bv.util as ut

class LinearRegression:
    def __init__(self,name,pathtodata):
        self.name=name
        self.logger=ut.getLog4jLogger(__name__)
    def learning(self):
        self.logger.info("call tostring")
    def toString(self):
        
        self.logger.info("call tostring")
        self.logger.debug("call tostring")
       