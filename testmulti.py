
import bv.test.MultiTest as test
import time

test.maxThreads = 10
starttime=time.time()*1000*1000
test.runTestTask(1000)
endtime=time.time()*1000*1000
print("time passed:"+str((endtime-starttime)/1000/1000)+" seconds")
