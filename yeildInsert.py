import time,asyncio,random

import os

from insert import connection, insert
from insertThread import insertThread
from test import test, ana
from file import temp,clearAll

db = connection()

def insertTemp():
    for line in open("./temp_goods"):
        insert(db, line)

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
    test(fileName)
    temp()
    # return asyncio.sleep(1)


    # clearAll()
def runInsert():
    sql_name = ['./temp_reviewsAndComments','./temp_assist', './temp_goods']
    # sql_name = ['./temp_goods']
    for master_name in sql_name:
        fileSize = os.path.getsize(master_name)
        if (fileSize != 0):
            insertTemp()
            # insertThread(master_name)
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
    write('/home/jingbao/桌面/result/')

if __name__ == '__main__':
    main()



