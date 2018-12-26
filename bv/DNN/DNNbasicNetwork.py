import bv.util.logger as log
import numpy as np
from bv.mult.worker import worker
import time
import random

class DNNBasicNetwork(worker):
    
    def buildNet(self):
        log.loginfo(" build network "+str(self.sigmoid(791)))

    def sigmoid(self,z):
        return 1.0/(1.0+np.exp(-z))


    def run(self):
        while(True):
            seed = random.randint(1,100)
            log.loginfo("cal sigmoid:"+self.sigmoid(seed).__str__()+" seed:"+seed.__str__())
            time.sleep(3)
