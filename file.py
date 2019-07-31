import json

import time

import os


def temp():
    sql_name = ['./assist', './goods', './reviewsAndComments']
    for file in sql_name:
        with open(file, "r+") as f:
            # f.truncate()  # 清空文件
            # file_size = os.path.getsize('./temp_' + file[2:len(file)])
            # while (file_size != 0):
            #     file_size = os.path.getsize('./temp_' + file[2:len(file)])
            #     time.sleep(2)
            os.remove('./temp_' + file[2:len(file)])
            os.rename(file, './temp_' + file[2:len(file)])
            os.mknod(file)
    return True

def clearAll():
    sql_name = ['./temp_assist', './temp_goods', './temp_reviewsAndComments']
    for file in sql_name:
        with open(file, "r+") as f:
            f.truncate()  # 清空文件
            f.close()
        # with open('./temp_' + file[2:len(file)], "r+") as f:
        #     f.truncate()  # 清空文件
        #     f.close()

    return True


def read():
    with open("./in.json", 'r') as load_f:
        load_dict = json.load(load_f)
        demps(load_dict)
    return load_dict


def write(path,sql):
    with open(path, 'a') as load_f:
        load_f.write(sql+'\n')
        return True
    return False

def demps(new_dict):
    with open("./in.json", "a") as f:
        json.dump(new_dict, f)
    print("加载入文件完成...")


def anaFile(inPath,outPath):
    start = time.time()
    flag=0
    inFile=None
    outFile=None
    if inPath==None:
        inFile=open("./in", "r")
    else:
        inFile=open(inPath,"r")
    if outPath == None:
        outFile = open("./out.json", "a")
    else:
        outFile = open(outPath, "a")
    outFile.write('[')
    flag = 0
    for line in inFile.readlines():
        # print(type(line))
        # line = line.strip('\n')
        # outFile.write(line)
        # print(line)

        if (flag == 0):
            line = line.strip()
            flag+=1
        else:
            if (line[0:6][2:5]=='_id'):
                line = line.replace("\n","")
                line = ',' + line
                # print('------------')
            # print(line[0:6][2:5])
        outFile.write(line.strip())
    outFile.write(']')
    end = time.time()
    print("耗时:", end - start)

#
# anaFile("/home/jingbao/桌面/result/功能饮料.json","/home/jingbao/桌面/功能饮料1.json")
# anaFile(None,None)


#
# files = os.listdir('/home/jingbao/桌面/result')
# for fileName in files:
#     anaFile("/home/jingbao/桌面/result/"+fileName, "/home/jingbao/桌面/temp/"+fileName)
# #



