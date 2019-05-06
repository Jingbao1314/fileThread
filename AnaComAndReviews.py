#sql insert into t_oem_taobao_com (reviews,comments) values
#c_v 是comments的信息
#r_v 是reviews的信息

import file
from mapping import  comMapping


def anaComAndReviews(skuid,c_list,r_list):
    sql=''
    res=False
    for index in range(len(c_list)):
        # c_json=json.loads(c_list[index])
        # r_json=json.loads(r_list[index])
        c_json=c_list[index]
        if index==0:
            sql=sql+ana_cloum(c_json)
        if index==len(c_list)-1:
            # if(r_list==None):
            #     sql = sql + ana_values(c_json,1) + ';'
            # else:
            #     sql = sql + ana_values(c_json,1) + ','
            sql = sql + ana_values(c_json, skuid,1) + ';'
        else:
            sql = sql + ana_values(c_json,skuid,1) + ','

    res=file.write("./reviewsAndComments", sql)
    sql=''
    if(r_list!=None):
        for r_index in range(len(r_list)):
            r_json = r_list[r_index]
            if r_index == 0:
                sql = sql + ana_cloum(r_json)
            if r_index == len(r_list) - 1:
                sql = sql + ana_values(r_json,skuid,2) + ';'
            else:
                sql = sql + ana_values(r_json,skuid,2) + ','



    return res|file.write("./reviewsAndComments",sql)


def ana_cloum(load_dict):
    sql_common = 'insert into t_oem_taobao_sku_comments (skuid,itype,'
    for key in load_dict.keys():
        # print(ana_com(key))
        if(key!='subobjects'):
            sql_common = sql_common + ana_com(key) + ','
        # sql_common = sql_common + key + ','
    # 遍历字典列表
    sql_common = sql_common[0:len(sql_common) - 1] + ') values '
    return sql_common

def ana_reviewsCloum(sql_reviews,load_dict):
    for key in load_dict.keys():
        sql_common = sql_reviews + key + ','
    # 遍历字典列表
    sql_common = sql_reviews[0:len(sql_common) - 1] + ') values '
    return sql_common




def ana_values(load_dict,skuid,itype):
    sql_common = '('+str(skuid)+','+str(itype)+','
    for key, values in load_dict.items():
        if(key!='subobjects'):
            if ((key == 'publishDate')):
                sql_common = sql_common + str(values).replace('\n','') + ','
            else:
                if (str(values) == 'None'):
                    sql_common = sql_common + 'NULL' + ','
                else:
                    if ('[' in str(values)):
                        sql_common = sql_common + '\'' + str(values).replace('\'', '\\\'').replace('\n','') + '\'' + ','
                    else:
                        sql_common = sql_common + '\'' + str(values).replace('\n','') + '\'' + ','
    sql_common = sql_common[0:len(sql_common) - 1] + ')'
    return sql_common


#获取对应的列
def ana_com(key):
    dict_mapping = comMapping()
    # print(dict_mapping)
    return dict_mapping[key]
