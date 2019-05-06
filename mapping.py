def goodsMapping():
    s = 'discount=discount,marketPrice=marketPrice,originPlace=originPlace,city=city,saleCount=saleCount,storehouse=storehouse,productBarcode=productBarcode,commentCount=commentCount,saleRank=saleRank,detailImageUrls=detailImageUrlsstr,queryWord=queryWord,videoUrls=videoUrlsstr,packing=packing,catId1=catId1,promotions=promotionsstr,monthSaleCount=monthSaleCount,warranties=warrantiesstr,mallType=mallType,sellerId=sellerId,productNo=productNo,sellerScreenName=sellerScreenName,brandName=brandName,storageMethod=storageMethod,price=price,url=url,lowPrice=lowPrice,producerId=producerId,description=description,catName2=catName2,shortTitle=shortTitle,soldout=soldout,catName1=catName1,userScreenName=userScreenName,publishDate=publishDate,publishDateStr=publishDateStr,ingredients=ingredients,catName3=catName3,licenseNumber=licenseNumber,catPathKey=catPathKey,coverUrl=coverUrl,likeCount=likeCount,nutrientContent=nutrientContent,id=id,openDate=openDate,tags=tags,stockSize=stockSize,brand=brand,title=title,saleStatus=saleStatus,brandId=brandId,catId3=catId3,province=province,rating=rating,weight=weight,logiRating=logiRating,servRating=servRating,descRating=descRating,factoryName=factoryName,highPrice=highPrice,address=address,expiryDate=expiryDate,publishDate=publishDate,imageUrls=imageurlsstr,userId=userId,catId2=catId2,appPrice=appPrice,_id=_id,favoriteCount=favoriteCount,subtitle=subtitle,producerName=producerName'
    s = s.replace(',', '=')
    list_map = s.split('=')
    dict_map = {}
    off = 0
    for index in range(int(len(list_map) / 2)):
        dict_map[list_map[off]] = list_map[off + 1]
        off += 2
    return dict_map

def skuMapping():
    s = 'price=price,id=id,services=services,stockSize=stockSize,keyValues=keyValuesstr,imageUrls=imageUrlsstr'
    s = s.replace(',', '=')
    list_map = s.split('=')
    dict_map = {}
    off = 0
    for index in range(int(len(list_map) / 2)):
        dict_map[list_map[off]] = list_map[off + 1]
        off += 2
    return dict_map

def comMapping():
    s='publishDate=publishDate,publishDateStr=publishDateStr,replies=repliesstr,url=url,subobjects=subobjects,commenterScreenName=commenterScreenName,referId=referId,likeCount=likeCount,rating=rating,appendComments=appendcommentsstr,tags=tags,id=id,commenterIdGrade=commenterIdGrade,content=content,commenterId=commenterId,imageUrls=imageurlsstr,source=source,commenterGradeName=commenterGradeName,commentCount=commentCount'
    s = s.replace(',', '=')
    list_map = s.split('=')
    dict_map = {}
    off = 0
    for index in range(int(len(list_map) / 2)):
        dict_map[list_map[off]] = list_map[off + 1]
        off += 2
    return dict_map

# print(comMapping())

# s='detailimageurls=detailimageurlsstr,warranties=warrantiesstr,videourls=videourlsstr,publishDate=publishDateStr,detailimageurls=detailimageurlsstr,imageurls=imageurlsstr'
# r='discount,marketPrice,originPlace,city,saleCount,storehouse,productBarcode,commentCount,saleRank,detailImageUrls,queryWord,videoUrls,packing,catId1,promotions,monthSaleCount,warranties,mallType,sellerId,productNo,sellerScreenName,brandName,storageMethod,price,url,lowPrice,producerId,description,catName2,shortTitle,soldout,catName1,userScreenName,publishDateStr,ingredients,catName3,licenseNumber,catPathKey,coverUrl,likeCount,nutrientContent,id,openDate,tags,stockSize,brand,title,saleStatus,brandId,catId3,province,rating,weight,logiRating,servRating,descRating,factoryName,highPrice,address,expiryDate,publishDate,imageUrls,userId,catId2,appPrice,_id,favoriteCount,subtitle,producerName'
# str_list=r.split(',')
# s=''
# for index in range(len(str_list)):
#     s=s+str_list[index]+'='+str_list[index]+','
# print(s)
