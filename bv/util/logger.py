import threading
import bv.util.datetime as dt
#threading.current_thread().setName("main producer #1")
log_file_path=""
def loginfo (*log):
    if log_file_path != "":
        print("load log trace, file path:"+log_file_path)
        logfile=open(log_file_path,"a+")
    else:
        print("not set log file, then no trace enabled");
    logs = " ("+threading.current_thread().getName()+")"+" message:"
    for l in log:
        logs += str(l)
    currentDate= dt.now()
    logfile.write("[ "+currentDate+" ]"+logs+"\n")
   # print("[ "+currentDate+" ]"+logs)


