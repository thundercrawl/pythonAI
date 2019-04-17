import logging
import bv.util as ut

class LinearRegression:
    def __init__(self,name,pathtodata):
        self.name=name
    def learning(self):
        ut.getCommonLogger().loginfo("call tostring")
    def toString(self):
        ut.getCommonLogger().loginfo("call tostring")
        ut.getLog4jLogger(__name__).info("call tostring")
       