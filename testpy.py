def checkSum(name,check=False):
    if check==True:
        print("check status is true")
    print("check name="+name)



checkSum('sujj')
checkSum('sujj',True)


class Util(object):
    def __init__(self,method=str)：
        self.method = method
