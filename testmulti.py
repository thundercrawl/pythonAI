
import bv.test.MultiTest as test
import bv.util.logger as log
import time
import requests
testurl = "http://www.baidu.com"

def taskHttp(testurl):
    starttime=time.time()*1000*1000
    r= requests.get(testurl)
    log.loginfo(r.status_code)
    endtime=time.time()*1000*1000
    log.loginfo("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
test.maxThreads = 10
starttime=time.time()*1000*1000
test.runTestTask(1000,taskHttp,testurl)
endtime=time.time()*1000*1000
print("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
