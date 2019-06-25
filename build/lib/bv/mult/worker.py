
import bv.util.logger as log
import threading
class worker:
    name=''
    def __init__(self,name):
        log.loginfo("init worker")
        self.name = name
        
        
    
    def run(self):
        raise NotImplementedError("work run function should been implemented by subclass")

    def getName(self):
        return self.name


class BasicNetWorker(worker):
    def run(self):
        log.loginfo("start basicnet worker")
        while(True):
            pass