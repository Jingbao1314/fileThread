import time

sql_goods=''
sql_goods = sql_goods +'\''+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'\''+ ');'



print(sql_goods)


line="insert into t_oem_taobao_sku "
if (('t_oem_taobao_sku_comments' in line) | ('t_oem_taobao_sku_options' in line)):
    pass
    # 关闭数据库连接
    # insert(db, line)
else:
    print("no")





