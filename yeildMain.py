import time,asyncio,random

import os

from insertThread import insertThread
from test import ana
from file import temp,clearAll

def runAna(fileName):
    sql_name = ['./temp_assist', './temp_goods', './temp_reviewsAndComments']
    for master_name in sql_name:
        fileSize = os.path.getsize(master_name)
        while True:
            if (fileSize != 0):
                time.sleep(5)
                fileSize = os.path.getsize(master_name)
            else:
                break
    ana(fileName)
    temp()
    return asyncio.sleep(1)
async def write(dirName):
    files = os.listdir(dirName)
    for fileName in files:
        print("writes")
        await runAna(dirName+fileName)

    # clearAll()
def runInsert():
    sql_name = ['./temp_assist', './temp_goods', './temp_reviewsAndComments']
    for master_name in sql_name:
        fileSize = os.path.getsize(master_name)
        if (fileSize != 0):
            insertThread(master_name)
    clearAll()
    return asyncio.sleep(1)
async def sql():
    flag=0
    while True:
        if(flag==0):
            flag+=1
            await asyncio.sleep(1)
        else:
            await runInsert()

write=write('/home/jingbao/桌面/json/')
sql=sql()

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        tasks = [sql,
        write
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        print('All fib finished.')
        loop.close()


