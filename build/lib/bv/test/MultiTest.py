import bv.util.logger as log
import threading
import time

exitFlag = 0
interval = 1
maxThreads=1
maxloop=1000
g_count=0
g_next=0
g_finished=0
g_finished_lock = threading.RLock()
g_lock = threading.RLock()
class WorkerThread (threading.Thread):
    def __init__(self, threadID, name, counter,taskm,testurl):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.taskm = taskm
        self.testurl=testurl
    def run(self):
        global maxloop
        self.counter = maxloop
        log.loginfo("Starting " + self.name)
        try:
            while self.counter>0:
                log.loginfo("running in the counter:"+str(self.counter))
                self.taskm(self.testurl)
                self.counter -=1
                increaseCounting()
        except Exception as e:
            log.loginfo("exception happened:"+e)

        finally:   
            log.loginfo("Exiting " + self.name)
            deFinished()

    # def submitTask(threadName, counter, delay):
    #     while counter:
    #         if exitFlag:
    #             threadName.exit()
    #         time.sleep(delay)
    #         print ("%s: %s" % (threadName, time.ctime(time.time())))
    #         counter -= 1

class TestMonitorThread(threading.Thread):
    def __init__(self,name,taskm):
        threading.Thread.__init__(self)
        self.name=name
        self.taskm=taskm
    def run(self):
        
        try:
            log.loginfo("start test monitor")
            while True:
                if (g_finished>0):
                    showCounting()
                else:
                    return
            
        except Exception as e:
            log.loginfo("exception happened:"+e)
        finally:
            log.loginfo("exit test monitor")
            pass
def runTestTask(taskn,taskm,testurl):
    # Create new threads
    global g_finished
    g_finished=taskn
    maxThreads=taskn
    global interval
    thread=TestMonitorThread("TestMonitor",showCounting)
    thread.start()
    while maxThreads > 0:
        thread=WorkerThread(maxThreads,"TestWorker"+str(maxThreads),3,taskm,testurl)
        thread.start()
        if(interval>0):
            time.sleep(interval)
        maxThreads -=1
    
    log.loginfo ("Exiting main call")
def exit():
    global g_finished
    try:
        while(True):
            if(g_finished):
                time.sleep(1)
            else:
                print("exit Test monitor")
                return
        
    except Exception as e:
        log.loginfo("exception:"+e)
    finally:
        log.loginfo("exit")

def increaseCounting():
    global g_count
    g_lock.acquire()
    g_count+=1
    g_lock.release()

def deFinished():
    global g_finished_lock
    global g_finished
    g_finished_lock.acquire()
    g_finished-=1
    g_finished_lock.release()

def showCounting():
    global g_next
    global g_count
    log.loginfo("current http request:"+str(g_count-g_next))
    g_next=g_count
    time.sleep(1)
