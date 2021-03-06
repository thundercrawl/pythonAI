
import bv.test.MultiTest as test
import bv.util as ut
import time
import requests
import sys
testurl = "http://www.baidu.com"
logger=ut.getLog4jLogger(__name__)
def taskHttp(testurl):
    r=None
    try:
        starttime=time.time()*1000*1000
        s = requests.session()
        s.keep_alive = False
        headers={
            'Content-Type':'application/json',
            'Connection':'close'
        }
        r= s.get(testurl,headers=headers,timeout=1)
        logger.info(r.status_code)
        endtime=time.time()*1000*1000
        logger.info("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
        r.close()
    except Exception as e:
        logger.info("Exception e:"+e.__str__)
    finally:
        if(r!=None):
            r.close()
        logger.info("exit method taskhttp, clear resources")


#main process
test.maxThreads = 10
starttime=time.time()*1000*1000
if(sys.argv.__len__() != 4):
    print("Not input correct parameters,sample: testmulty.py http://www.baidu.com c:/trace.log 5")
    sys.exit("Error occurred")
testurl=sys.argv[1]
log.log_file_path = sys.argv[2]
print("read test url:"+sys.argv[1])
taskn=sys.argv[3]
test.runTestTask(int(taskn),taskHttp,testurl)
endtime=time.time()*1000*1000
print("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
