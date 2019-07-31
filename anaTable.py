import json

fileName='/home/jingbao/桌面/其他/python学习资料/框架test/Analysis_json/outTable'
# with open(fileName, 'r') as load_f:
#     load_dict_list = json.load(load_f, strict=False)
# # print(load_dict_list['trades'])
# res='名称 类型 示例值 描述\n'
# for load_dict in load_dict_list:
#     if(load_dict=='trades'):
#         dic=load_dict_list['trades']['trade'][0]
#         for key in dic:
#             if(type(dic[key])==bool):
#                 if(dic[key]):
#                     res = res + key + ' xx ' + 'True' + ' xxx\n'
#                 else:
#                     res = res + key + ' xx ' + 'False' + ' xxx\n'
#             else:
#                 if(str(dic[key]).find('-')<0):
#                     res = res + key + ' xx ' + str(dic[key]).replace(' ','') + ' xxx\n'
#                 else:
#                     res = res + key + ' xx ' + str(dic[key]).replace(' ','*') + ' xxx\n'
#         print(res)

file = open(fileName)
for line in file:
    if('-' in line):
        print(line.replace(' ', '*').replace('\n', ''))
    else:
        print(line)
