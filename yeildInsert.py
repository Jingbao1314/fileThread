import time,asyncio,random

import os

from insertThread import insertThread
from test import ana
from file import temp,clearAll

def runAna(fileName):
    print('runAna')
    # sql_name = ['./temp_assist', './temp_goods', './temp_reviewsAndComments']
    # for master_name in sql_name:
    #     fileSize = os.path.getsize(master_name)
    #     while True:
    #         if (fileSize != 0):
    #             print('runAna')
    #             time.sleep(5)
    #             fileSize = os.path.getsize(master_name)
    #         else:
    #             break
    ana(fileName)
    temp()
    # return asyncio.sleep(1)


    # clearAll()
def runInsert():
    sql_name = ['./temp_reviewsAndComments','./temp_assist', './temp_goods']
    for master_name in sql_name:
        fileSize = os.path.getsize(master_name)
        if (fileSize != 0):
            insertThread(master_name)
    clearAll()
    # return asyncio.sleep(1)

def sql():
    flag=0
    while True:
        flag=yield flag
        runInsert()

def write(dirName):
    s=sql()
    s.send(None)
    files = os.listdir(dirName)
    for fileName in files:
        print("writes")
        runAna(dirName+fileName)
        s.send(None)


def main():
    write('/home/jingbao/桌面/temp/')

if __name__ == '__main__':
    main()



