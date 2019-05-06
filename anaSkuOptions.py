

import file
from mapping import skuMapping


def anaSkuOptions(s_list,skuid):
    sql=''
    for index in range(len(s_list)):
        s_json=s_list[index]
        if index==0:
            sql=sql+ana_cloum(s_json)
        if index==len(s_list)-1:
            sql = sql + ana_values(s_json,skuid) + ';'
        else:
            sql = sql + ana_values(s_json,skuid) + ','

    # if(sql[len(sql)-1:len(sql)]==','):
    #     sql = sql[0:len(sql) - 1]

    return file.write("./assist",sql)

def ana_cloum(load_dict):
    sql_common = 'insert into t_oem_taobao_sku_options (skuid,'
    for key in load_dict.keys():
        sql_common = sql_common + skuMap(key) + ','
        # sql_common = sql_common + key + ','
    # 遍历字典列表
    sql_common = sql_common[0:len(sql_common) - 1] + ') values '
    return sql_common


def ana_values(load_dict,skuid):
    not_str_cloum='price,stockSize'
    sql_sku = '('+str(skuid)+','
    for key, values in load_dict.items():
        if (key in not_str_cloum):
            if (str(values) == 'None'):
                sql_sku = sql_sku + 'NULL' + ','
            else:
                sql_sku = sql_sku + str(values).replace('\n','') + ','
        else:
            if ('[' in str(values)):
                sql_sku = sql_sku + '\'' + str(values).replace('\'', '\\\'').replace('\n','') + '\'' + ','
            else:
                if (str(values) == 'None'):
                    sql_sku = sql_sku + 'NULL' + ','
                else:
                    sql_sku = sql_sku + '\'' + str(values).replace('\n','') + '\'' + ','
    sql_sku = sql_sku[0:len(sql_sku) - 1] + ')'
    return sql_sku


def skuMap(key):
    dict_mapping=skuMapping()
    return dict_mapping[key]

