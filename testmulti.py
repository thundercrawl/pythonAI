
import bv.test.MultiTest as test
import bv.util.logger as log
import time
import requests
import sys
testurl = "http://www.baidu.com"

def taskHttp(testurl):
    starttime=time.time()*1000*1000
    r= requests.get(testurl)
    log.loginfo(r.status_code)
    endtime=time.time()*1000*1000
    log.loginfo("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
test.maxThreads = 10
starttime=time.time()*1000*1000
if(sys.argv.__len__() == 1):
    print("Not input test url,sample: http://www.baidu.com")
    sys.exit("Error occurred")
testurl=sys.argv[1]
print("read test url:"+sys.argv[1])
test.runTestTask(1000,taskHttp,testurl)
endtime=time.time()*1000*1000
print("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
