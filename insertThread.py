# -*- coding: utf-8 -*-
import os, time
import threading

from insert import insert, connection

rlock = threading.RLock()

curPosition = 0  # 初始化位置为文件其实位置


class Reader(threading.Thread):
    def __init__(self, res):
        self.res = res
        super(Reader, self).__init__()  # 调用子类构造函数获得文件大小

    def run(self):  # 线程函数
        global curPosition
        fstream = open(self.res.fileName, 'r')  # 打开文件
        while True:
            print('sql---run')
            rlock.acquire()
            startPosition = curPosition  # 每次更新起始位置
            if (startPosition + self.res.fileSize / 2) < self.res.fileSize:  # 这里，例如开了10个线程，就将文件分为10块，每个线程负责一块
                curPosition = endPosition = (startPosition + self.res.fileSize / 2)
            else:
                curPosition = endPosition = self.res.fileSize
            rlock.release()

            if startPosition == self.res.fileSize:
                break
            elif startPosition != 0:  # 这种情况适用于除了第一个文件块之后的文件块，因为分割后，第一块以后的文件块的起始位置肯定比0大
                fstream.seek(startPosition)  # 找到那个位置
                line = fstream.readline()  # 由于这一行在上一个循环中已经读取了，所以先读一行，把这行跳过
            pos = fstream.tell()  # 获取当前的位置
            db = connection()
            while pos <= endPosition:
                line = fstream.readline()
                # print(line)
                # if (('t_oem_taobao_sku_comments' in line)):
                #     insert(db, line)
                #     # print("t_oem_taobao_sku_comments")
                #
                #
                # if (('t_oem_taobao_sku_options' in line)):
                #     insert(db, line)
                    # print("t_oem_taobao_sku_comments")

                insert(db, line)
                # if (('t_oem_taobao_sku_comments' in line)|('t_oem_taobao_sku_options' in line)):
                #    print("")
                #     # 关闭数据库连接
                #     # insert(db, line)
                # else:
                #     insert(db, line)


                '''
                    对每一行进行处理
                '''
                pos = fstream.tell()  # 每处理一行，更新坐标
                print(pos,'------------------------------------------',self.res.fileSize)
                if pos == self.res.fileSize:  # 如果读到了文件末尾，跳出循环
                    db.close()
                    break


        fstream.close()


class Resource(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.getFileSize()

    # 计算文件大小
    def getFileSize(self):
        fstream = open(self.fileName, 'r')
        fstream.seek(0, 2)  # 这里0代表文件开始，2代表文件末尾
        self.fileSize = fstream.tell()
        fstream.close()



def insertThread(fileName):
    # 读取配置文件，配置文件里面可以写一些文件的信息，这样方便修改
    # config = ConfigParser.ConfigParser()
    # config.readfp(open('conf.ini'))
    # fileName = config.get("info", "fileRead")
    starttime = time.clock()
    # 线程数
    # threadNum = int(config.get("info", "threadNum"))
    # # 文件
    # fileName = './assist'
    res = Resource(fileName)
    print('res.fileName',res.fileName)
    threadNum = 2
    threads = []
    # 初始化线程
    for i in range(threadNum):
        rdr = Reader(res)
        threads.append(rdr)
    # 开始线程
    for i in range(threadNum):
        curPosition=0
        threads[i].start()
    # 结束线程
    for i in range(threadNum):
        threads[i].join()

    print(time.clock() - starttime)
# if __name__ == '__main__':
#
#     # 读取配置文件，配置文件里面可以写一些文件的信息，这样方便修改
#     # config = ConfigParser.ConfigParser()
#     # config.readfp(open('conf.ini'))
#     # fileName = config.get("info", "fileRead")
#     starttime = time.clock()
#     # 线程数
#     # threadNum = int(config.get("info", "threadNum"))
#     # # 文件
#     fileName = './assist'
#     res = Resource(fileName)
#     threadNum = 2
#     threads = []
#     # 初始化线程
#     for i in range(threadNum):
#         rdr = Reader(res)
#         threads.append(rdr)
#     # 开始线程
#     for i in range(threadNum):
#         threads[i].start()
#     # 结束线程
#     for i in range(threadNum):
#         threads[i].join()
#
#     print(time.clock() - starttime)