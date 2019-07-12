import jieba
import bv.util.stringUtil as strUtils


def prepare():
    with open("C:/temp/wiki_00/wiki_00", 'r', encoding="utf8") as file:
        for line in file:
            print(line)


def main():
    with open("c:/temp/1.txt", 'r', encoding="utf8") as file:
        textcn = file.read().replace('\n', '')
    rtcn = jieba.cut(textcn)
    print("object:" + str(rtcn))

    temp = "/".join(rtcn)
    #print(temp)
    temp = strUtils.removePunctuationMarks(temp)
    print(temp)
    print(temp.__len__())


if __name__ == '__main__':
    prepare()
    main()