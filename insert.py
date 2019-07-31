#!/usr/bin/python3

import pymysql

from file import write


def connection():
   # 打开数据库连接
   db = pymysql.connect(host='123.56.194.146', port=3306, user='lechundbuser', passwd='UIOP!@#$LechuN', db='lechun_erp_micro_service', charset='utf8')
   return db


def insert(db,sql):

   # 使用cursor()方法获取操作游标
   cursor = db.cursor()
   print("insert")

   try:
      # 执行sql语句
      cursor.execute(sql)
      # 提交到数据库执行
      print(db.commit())

      print("insert OK")
   except:
      print(sql)
      if(sql!="\n"):
          write('./error.sql', sql)

      # 如果发生错误则回滚
      db.rollback()

