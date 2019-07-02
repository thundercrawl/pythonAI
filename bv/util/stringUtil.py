import re


def removePunctuationMarks(temp, split="/"):
    strs = temp.split(split)
    string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",
                    temp)
    print(strs.__len__())
    print(type(strs))
    rlist = []
    for s in strs:
        judge = True
        for ch in s:
            if u'\u4e00' <= ch <= u'\u9fff':
                a = {}
            else:
                judge = False
        if judge == True:
            rlist.append(s)
    return rlist
