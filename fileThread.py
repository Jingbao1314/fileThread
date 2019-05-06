# _*_coding:utf-8_*_
import time, threading

import os

from insert import connection, insert

'''
Reader类，继承threading.Thread
@__init__方法初始化
@run方法实现了读文件的操作
'''
class Reader(threading.Thread):
    def __init__(self, file_name, start_pos, end_pos):
        super(Reader, self).__init__()
        self.file_name = file_name
        self.start_pos = start_pos
        self.end_pos = end_pos

    def run(self):
        fd = open(self.file_name, 'r')
        '''
        该if块主要判断分块后的文件块的首位置是不是行首，
        是行首的话，不做处理
        否则，将文件块的首位置定位到下一行的行首
        '''
        if self.start_pos != 0:
            fd.seek(self.start_pos-1)
            if fd.read(1) != '\n':
                line = fd.readline()
                self.start_pos = fd.tell()
        fd.seek(self.start_pos)
        '''
        对该文件块进行处理
        '''
        db=connection()
        while (self.start_pos <= self.end_pos):
            line = fd.readline()
            '''
            do somthing
            '''
            if('insert' in line):
                # 关闭数据库连接
                insert(db,line)
            self.start_pos = fd.tell()

        db.close()

'''
对文件进行分块，文件块的数量和线程数量一致
'''
class Partition(object):
    def __init__(self, file_name, thread_num):
        self.file_name = file_name
        self.block_num = thread_num

    def part(self):
        fd = open(self.file_name, 'r')
        fd.seek(0, 2)
        pos_list = []
        file_size =  os.path.getsize(self.file_name)
        block_size = file_size/self.block_num
        # print('self.file_name',self.file_name)
        # print('fileSize',file_size)
        # print('block_size', block_size)
        start_pos = 0
        for i in range(self.block_num):
            if i == self.block_num-1:
                end_pos = file_size-1
                pos_list.append((start_pos, end_pos))
                break
            end_pos = start_pos+block_size-1
            if end_pos >= file_size:
                end_pos = file_size-1
            if start_pos >= file_size:
                break
            pos_list.append((start_pos, end_pos))
            start_pos = end_pos+1
        fd.close()
        return pos_list

if __name__ == '__main__':
    '''
    读取配置文件
    '''
    # config = ConfigParser.ConfigParser()
    # config.readfp(open('conf.ini'))
    #文件名
    file_name = './assist'
    #线程数量
    thread_num = 2
    #起始时间
    start_time = time.clock()
    p = Partition(file_name, thread_num)
    t = []
    pos = p.part()
    print(pos)
    #生成线程
    for i in range(thread_num):
        t.append(Reader(file_name, *pos[i]))
    #开启线程
    for i in range(thread_num):
        t[i].start()
    for i in range(thread_num):
        t[i].join()
    #结束时间
    end_time = time.clock()
    print ("Cost time is %f" % (end_time - start_time))