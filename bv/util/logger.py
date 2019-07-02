import threading
from . import datetime as dt
#threading.current_thread().setName("main producer #1")
log_file_path = ""
logfile = None


def loginfo(*log):
    global log_file_path
    global logfile
    if log_file_path != "" and logfile == None:
        print("load log trace, file path:" + log_file_path)
        logfile = open(log_file_path, "a+")
    else:
        print("use default path d:/trace.log")
        logfile = open("c:/trace.log", "a+")
    logs = " (" + threading.current_thread().getName() + ")" + " message:"
    for l in log:
        logs += str(l)
    currentDate = dt.now()
    logfile.write("[ " + currentDate + " ]" + logs + "\n")


# print("[ "+currentDate+" ]"+logs)
