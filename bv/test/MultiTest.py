import bv.util.logger as log
import threading
import time
log.log_file_path='d://trace.log'
exitFlag = 0
interval = 1
maxThreads=1
maxloop=1000
class WorkerThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global maxloop
        log.loginfo("Starting " + self.name)
        try:
            while self.counter>0:
                log.loginfo("running in the counter:"+str(self.counter))
                time.sleep(interval)
                self.counter -=1
        except Exception as e:
            log.loginfo("exception happened:"+e)

        finally:   
            log.loginfo("Exiting " + self.name)
    # def submitTask(threadName, counter, delay):
    #     while counter:
    #         if exitFlag:
    #             threadName.exit()
    #         time.sleep(delay)
    #         print ("%s: %s" % (threadName, time.ctime(time.time())))
    #         counter -= 1


def runTestTask(taskn):
    # Create new threads
    maxThreads=taskn
    global interval

    while maxThreads > 0:
        thread=WorkerThread(maxThreads,"TestWorker"+str(maxThreads),3)
        thread.start()
        if(interval>0):
            time.sleep(interval)
        maxThreads -=1
    
    log.loginfo ("Exiting main call")