import json

import time

import file
from AnaComAndReviews import anaComAndReviews
from anaSkuOptions import anaSkuOptions
from mapping import goodsMapping
def goodsMap(key):
    dict_mapping=goodsMapping()
    return dict_mapping[key]

# test_string = '{"com": "com_value", "goods": "goods_values", "assist": "assist_values"}'
# test_json=json.loads(test_string)
# print(test_json.keys())
# print(test_json.__len__())
# print(type(test_json.items()))




def ana(fileName):

    print("************************ana")
    start = time.time()
    load_dict = {}
    with open(fileName, 'r') as load_f:
        load_dict_list = json.load(load_f, strict=False)
        # print(load_dict)
    # com_have = False
    # sku_have = False
    for load_dict in load_dict_list:
        com_have = False
        sku_have = False
        rev_have = False
        for key in load_dict.keys():
            if key == 'reviews':
                rev_have = True
            elif key == 'comments':
                com_have = True
            elif key == 'skuOptions':
                sku_have = True

        c_list = None
        r_list = None
        if (com_have):
            c_list = list(load_dict["comments"])
        if (rev_have):
            r_list = list(load_dict["reviews"])

        if (com_have | rev_have):
            print(anaComAndReviews(load_dict['id'], c_list, r_list))

        if (sku_have):
            s_list = list(load_dict["skuOptions"])
            print(anaSkuOptions(s_list, load_dict['id']))

        sql_goods = 'insert into t_oem_taobao_sku ('
        not_have = 'barcode,buyMaxCount,activityPrice,presales,coverUrl,_id,description'
        for key in load_dict.keys():
            if key == 'reviews':
                pass
            elif key == 'comments':
                pass
            elif key == 'skuOptions':
                pass
            else:

                if(key=='id'):
                    sql_goods = sql_goods + goodsMap(key) + ','
                if (key not in not_have):
                    sql_goods = sql_goods + goodsMap(key) + ','
                # if ((key != 'barcode') & (key != 'buyMaxCount')):
                #     sql_goods = sql_goods + goodsMap(key) + ','
                    # sql_goods = sql_goods + key + ','

        # 遍历字典列表
        # sql_goods = sql_goods[0:len(sql_goods) - 1] + ') values ('
        sql_goods = sql_goods+'time' + ') values ('
        not_str_cloum = 'servRating,favoriteCount,logiRating,discount,saleCount,rating,marketPrice,highPrice,lowPrice,price,descRating,appPrice,monthSaleCount,mallType,likeCount,commentCount,expiryDate'
        for key, values in load_dict.items():
            # print(key)
            # print(values)
            if key == 'reviews':
                print("")
            elif key == 'comments':
                print("")
            elif key == 'skuOptions':
                print("")
            else:
                if (key == 'id'):
                    sql_goods = sql_goods + str(values).replace('\n', '') + ','
                if(key not in not_have):
                    if (key in not_str_cloum):
                        if (str(values) == 'None'):
                            sql_goods = sql_goods + 'NULL' + ','
                        else:
                            sql_goods = sql_goods + str(values).replace('\n', '') + ','
                    else:
                        if ('[' in str(values)):
                            sql_goods = sql_goods + '\'' + str(values).replace('\'', '\\\'').replace('\n',
                                                                                                     '') + '\'' + ','
                        else:
                            if (str(values) == 'None'):
                                sql_goods = sql_goods + 'NULL' + ','
                            else:
                                sql_goods = sql_goods + '\'' + str(values).replace('\n', '') + '\'' + ','

        # sql_goods = sql_goods[0:len(sql_goods) - 1] + ');'
        sql_goods = sql_goods +'\''+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'\''+ ');'
        file.write("./goods", sql_goods)

    end = time.time()
    print(end - start)
# ana('/home/jingbao/桌面/temp/进口巧克力.json')

def test(fileName):
    num=0
    inFile = open(fileName, "r")
    for line in inFile.readlines():
        load_dict = json.loads(line)
        com_have = False
        sku_have = False
        rev_have = False
        for key in load_dict.keys():
            if key == 'reviews':
                rev_have = True
            elif key == 'comments':
                com_have = True
            elif key == 'skuOptions':
                sku_have = True

        c_list = None
        r_list = None
        if (com_have):
            c_list = list(load_dict["comments"])
        if (rev_have):
            r_list = list(load_dict["reviews"])

        # if (com_have | rev_have):
        #     print(anaComAndReviews(load_dict['id'], c_list, r_list))
        #
        # if (sku_have):
        #     s_list = list(load_dict["skuOptions"])
        #     print(anaSkuOptions(s_list, load_dict['id']))

        sql_goods = 'insert into t_oem_taobao_sku ('
        not_have = 'barcode,buyMaxCount,activityPrice,presales,coverUrl,_id,description,keyValues'
        for key in load_dict.keys():
            if key == 'reviews':
                pass
            elif key == 'comments':
                pass
            elif key == 'skuOptions':
                pass
            else:
                if (key == 'id'):
                    sql_goods = sql_goods + goodsMap(key) + ','
                if (key not in not_have):
                    sql_goods = sql_goods + goodsMap(key) + ','
                    # if ((key != 'barcode') & (key != 'buyMaxCount')):
                    #     sql_goods = sql_goods + goodsMap(key) + ','
                    # sql_goods = sql_goods + key + ','

        # 遍历字典列表
        # sql_goods = sql_goods[0:len(sql_goods) - 1] + ') values ('
        sql_goods = sql_goods + 'time) values ('
        not_str_cloum = 'servRating,favoriteCount,logiRating,discount,saleCount,rating,marketPrice,highPrice,lowPrice,price,descRating,appPrice,monthSaleCount,mallType,likeCount,commentCount,expiryDate'
        for key, values in load_dict.items():
            # print(key)
            # print(values)
            if key == 'reviews':
                print("")
            elif key == 'comments':
                print("")
            elif key == 'skuOptions':
                print("")
            else:
                if (key == 'id'):
                    sql_goods = sql_goods + str(values).replace('\n', '') + ','
                if (key not in not_have):
                    if (key in not_str_cloum):
                        if (str(values) == 'None'):
                            sql_goods = sql_goods + 'NULL' + ','
                        else:
                            sql_goods = sql_goods + str(values).replace('\n', '') + ','
                    else:
                        if ('[' in str(values)):
                            sql_goods = sql_goods + '\'' + str(values).replace('\'', '\\\'').replace('\n',
                                                                                                     '') + '\'' + ','
                        else:
                            if (str(values) == 'None'):
                                sql_goods = sql_goods + 'NULL' + ','
                            else:
                                sql_goods = sql_goods + '\'' + str(values).replace('\n', '') + '\'' + ','

        # sql_goods = sql_goods[0:len(sql_goods) - 1] + ');'
        sql_goods = sql_goods+'\'' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\'' + ');'

        file.write("./goods", sql_goods)
        num = num + 1
    file.write("./test", str(num))

# test('/home/jingbao/桌面/result/功能饮料.json')