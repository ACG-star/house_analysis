# #备注
# with基于上下文，会自动帮助我们关闭文件。
# 如果不关闭文件，会怎么样？对于在个人电脑上没什么影响。如果你执行的python程序结束了，文件会自动关闭。
# 服务器端如果不关闭文件，会出现句柄泄露，导致句柄耗尽。
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






# for i in range(1,8):
#     i = str(i)
#     baseurl = "https://ny.fang.anjuke.com/loupan/all/p"
#     baseurl = baseurl + i +"/"
#     print(baseurl)
#
#

# import requests
#
# url = "https://www.runoob.com/python/att-string-format.html"
# # 添加headers信息，信息包括（操作系统信息NT，客户端(浏览器)信息），headers为字典格式，首尾不能存在空格
# headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
# }
# response = requests.get(url, headers=headers).text  # 使用requests库get请求，加入参数headers信息
# with open(r'F:\test.txt', 'ab') as fw:  # 使用a追加，保留每页数据
#     fw.write(str(response).encode("utf-8"))
# # print("开始写入……！")
# wt.write(key.encode("utf-8")+"\n")
#                             # 关于‘+”\n"’：列表写入时列表中的每个元素不会自动添加换行符
#                             # 因此通常需要在列表的每个元素后面添加换行符以确保写入的文件会分行
#                             # 且列表中必须是字符串格式

#结构：[div class=item-mod]
#          [div class=infos]
#               [a class=lp-name]
#                   [span class=items-name]         小区名
#               [a class=address]
#                   [span class=list-map]           小区地址
#               [a class=huxing]
#                   [span]                          户型
#                   [span class=building-area]      建筑面积
#           [a class=favor-pos]
#               [p class=price]
#                   [span]                          价格
#
# #
# def writeCsv(List,f,num):
#     for data in List:
#         csvwrite = csv.writer(f)
#         if num ==1:
#             csvwrite.writerow([data])
#         elif num ==2:
#             csvwrite.writerow(["",data,"",""])
#         elif num ==3:
#             csvwrite.writerow(["","",data,""])
#         elif num ==4:
#             csvwrite.writerow(["","","",data])


#目前处理数据方法效率很低，原因：400个数据，四次筛选+四次re
#数据清洗test
from bs4 import BeautifulSoup
import re
import csv

with open(r'F:\test.txt', 'rb') as fr:
    code = fr.read().decode("utf-8")
bs = BeautifulSoup(str(code),"html5lib")
itemListAll = bs.find_all("div", attrs={"class": "item-mod"})   #ListAll是包含所有信息的多个列表

for item in itemListAll[1:380]:
    #因为csv写入时格式为列表嵌套，最终结果中列表格式[]无法去除，因此for循环嵌套取元素，最终写入
    #小区名信息提取、清洗及取元素，以备存储使用
    # nameList = item.find(attrs={"class": "items-name"})
    # # print(name)#<span class="items-name">建业碧桂园龙悦城</span>
    # ruleName = re.compile('">(.*?)</')
    # nameInfos = re.findall(ruleName, str(nameList))
    # for name in nameInfos:

    #地址信息提取、清洗及取元素，以备存储使用
    addressList = item.select(".list-map")  # 包含所有地址信息的多个列表
    # print(address)#[<span class="list-map" target="_blank">[ 宛城区 宛城区 ] 雪枫路与仲景南路交叉口南侧</span>]
    ruleAddress = re.compile('">(.*?)</')  # 优化结束写个函数统一调用
    addressInfos = re.findall(ruleAddress, str(addressList).replace(u'\xa0', u'o'))  # 芜湖，nice
    # print(addressList)#['[\xa0宛城区\xa0宛城区\xa0]\xa0独山大道与光武路交会处西北角'] #\xa0 是不间断空白符 &nbsp;
    for addressData in addressInfos:
        # print(address)#[o宛城区o宛城区o]o雪枫路与仲景南路交叉口南侧
        ruleRegion = re.compile('o(.*?)o') #region:行政区
        addressResult = re.search(ruleRegion,str(addressData)) #search 返回检索到的第一个结果 Result:结果
        address = addressResult.group(1)

        #新房类型
        typeList = item.select(".wuyetp")
        ruleType = re.compile('">(.*?)</')
        typeInfos = re.findall(ruleType,str(typeList))
        for typ in typeInfos:
            # 关键词
            keyList = item.select(".tag")
            ruleKey = re.compile('">(.*?)</')
            keyInfos = re.findall(ruleKey, str(keyList))
            for key in keyInfos:
                print()
            #
            # #建筑面积提取、清洗及取元素，以备存储使用
            # areaList = item.select(".building-area")
            # ruleArea = re.compile('">(.*?)</span>')  # <span class="building-area">建筑面积：110-142㎡</span>
            # areaInfos = re.findall(ruleArea, str(areaList))
            # for area in areaInfos:
            #
            #     #每平方价格信息提取、清洗及取元素，以备存储使用
            #     priceList = item.select("a > p")
            #     # print(price)
            #     rulePrice = re.compile('<span>(.*?)</span>')
            #     priceInfos = re.findall(rulePrice, str(priceList))
            #     for price in priceInfos:
            #         #最终写入
            #         with open(r"F:\房源基础数据.csv", "a", newline="", encoding="utf-8") as f:
            #             csvwrite = csv.writer(f)
            #             csvwrite.writerow([name, address, area, price])
                        # csvwrite.writerow([name, address,typ,area, price])

    # # 使用循环遍历获取所需信息   #不采用for循环嵌套的方法：四个400次的for循环时间复杂度是，400^400过于庞大
        # csvwrite = csv.writer(f)
        # csvwrite.writerow([nameList, addressList, areaList, priceList])  # 写入时 格式必须为列表













# itemListAll = bs.find_all("div", attrs={"class": "item-mod"})  #[,,,,,,,,,]
# # print(itemListAll[2:5])
# # print(len(itemListAll))#496组数据
# # print(type(itemListAll))
# # itemListAll = BeautifulSoup(str(itemListAll),"html5lib")
#
# for item in itemListAll[1:30]:
#     # print(item)#前两个是空的
#     address = item.select(".list-map")
#     # print(address)#[<span class="list-map" target="_blank">[ 宛城区 宛城区 ] 雪枫路与仲景南路交叉口南侧</span>]
#     ruleAddress = re.compile('">(.*?)</')  #优化结束写个函数统一调用
#     addressList = re.findall(ruleAddress, str(address).replace(u'\xa0', u' '))#芜湖，nice
#     # print(addressList)#['[\xa0宛城区\xa0宛城区\xa0]\xa0独山大道与光武路交会处西北角'] #\xa0 是不间断空白符 &nbsp;
#
#     name = item.find(attrs={"class":"items-name"})
#     # print(name)#<span class="items-name">建业碧桂园龙悦城</span>
#     ruleName = re.compile('">(.*?)</')
#     nameList = re.findall(ruleName,str(name))
#
#     area = item.select(".building-area")
#     ruleArea = re.compile('">(.*?)</span>')#<span class="building-area">建筑面积：110-142㎡</span>
#     areaList = re.findall(ruleArea, str(area))
#
#     price = item.select("a > p")
#     # print(price)
#     rulePrice = re.compile('<span>(.*?)</span>')
#     priceList = re.findall(rulePrice, str(price))
#     print(priceList)
#     # print(len(priceList))
#     # print(price)  ####验证Beautiful处html参数到底要不要str类型->要！

    # itemListAll = BeautifulSoup(str(itemListAll),"html5lib") #二次bs
    # #关于使用str的备注：bs后的结果是一个标签集合[bs4.element.ResultSet]，类似于列表，bs可以对字符串类型进行解析
    # (对html源码分析时可不加，但对bs后的结果再次进行bs分析时要加，否则会报类型不匹配)【TypeError: a bytes-like object is required, not 'ResultSet'】
    # #bs4库 是解析、遍历、维护、“标签树“的功能库，也就是：bs4库把html源代码重新进行了格式化，


    # rulePrice = price.replace(' ','')
    # price = BeautifulSoup(str(price), "html5lib") #TypeError: a bytes-like object is required, not 'ResultSet'
    # print(price.text.replace('\n','').replace(' ',''))#!!!可行！！替换两次
    # priceList = price.text.replace('\n', '').replace(' ', '')
#暂时没用的
    # for p in price:
    #     test = BeautifulSoup(str(p),"html5lib")
    #     # if test.text == '售价待定':
    #     #     print()
    #     print(test.text)
    # for alist in areaList:
    #     print(alist)
    # #遍历列表
    # for name in nameList:
    #     print(name)
    #.find("span",attrs={"class":"list-map"})
    # huxing = item.find(attrs={"class":"huxing"})
    # # print(huxing)
    # #target="_blank">户型：<span>3室</span>/<span>4室</span><em class="diving-line"></em>
    # ruleHuxing = re.compile('>(.*?)</span>')
    # huxingList = re.findall(ruleHuxing, str(huxing))
    # # print(huxingList)
    # for hx in huxingList:
    #     print(hx)






    # print(price)
    # [ < p class ="price" > 均价 < span > 8500 < / span > 元 / ㎡ < / p >]
    # [< p class ="price-txt" > 售价待定 < / p >, < p class ="favor-tag around-price" > 周边均价 < span > 9100 < / span > 元 /㎡ < / p >]
    # print([name,address,huxing,area,price])

 # with open(r'F:\test.txt', 'wb') as fw:
    #     fw.write(bs.encode("utf-8"))

#csv写入格式
    # import csv
    # with open(“lagou.csv”,‘w’,encoding=‘utf8’,newline=’\n’) as f:
    # writer=csv.writer(f)
    # writer.writerow(list)



#     with open(r'F:\test.csv', "w", encoding='utf8', newline='\n') as f:
#         writer=csv.writer(f)
#         writer.writerow([name,address,huxing,area,price])
# #

# itemListAll = BeautifulSoup(str(itemListAll),"html5lib")
#
#
#
#
# # itemListAll_list = itemListAll.select("div div a span")
# itemName_list = itemListAll.select(".items-name")#标签选择器(a)、类选择器(.)、id选择器(#)
# # for data in itemName_list[1:]:
# #     print(data.text) #text全拿出来
# # print("name:",len(itemName_list))   #478
# itemMap_list = itemListAll.select(".list-map")
# # print("map:",len(itemMap_list))     #478
# # for data in itemMap_list[1:]:
# #     print(data.text) #text全拿出来
# itemArea_list = itemListAll.select(".building-area")
# # print("area:",len(itemArea_list))   #477  #第五页最后一个花溪园
# # for data in itemArea_list[1:]:
# #     print(data.text) #text全拿出来#
# itemPrice_list = itemListAll.select("a > p")   #itemPrice_list = itemListAll.select(".price")#少20个数据
# # print("price:",len(itemPrice_list)) #578
# # for data in itemPrice_list[1:]:
# #     print(data.text) #text全拿出来
# info =[]
# with open(r'F:\test.csv',"w",encoding='utf8',newline='\n') as f:
#     writer=csv.writer(f)
#     writer.writerow(list)

#
# addressList1 = ["甘雨","璃月第一冰弓手","小麒麟","王小美","琉璃百合","七七","阿莫斯嘿嘿，嘿嘿阿莫斯",]
# addressList2 = ["安伯","蒙德第一火弓手","兔兔伯爵","兔兔炸矿","离谱离谱","黎明神剑","原神yyds",]
# addressList = [addressList1,addressList2]
# print(addressList)
# address = ",".join(addressList)




#
#旧版本
# commentItemListAll = bs.find_all("div", attrs={"class": "item-mod"})
# # print(len(commentItemListAll))   #len()->496个
# bs = BeautifulSoup(str(commentItemListAll), "html5lib")
# # 详细信息div
# commentItemListInfos = bs.find_all("div", attrs={"class": "infos"})
# # print(len(commentItemListInfos))  # 为许多个class=infos的div，格式：列表  len()-> 480个
# # 价格信息div
# commentItemListPrice = bs.find_all("a", attrs={"class": "favor-pos"})
# print(len(commentItemListPrice))  # 为许多个class=price的p标签  len()->478个
#旧版本
#

# itemName_list = itemListAll.select(".items-name")  # 标签选择器(a)、类选择器(.)、id选择器(#)
    # for data in itemName_list[1:]:
    #     print(data.text) #text全拿出来
    # print("name:", len(itemName_list))  # 478
    # itemMap_list = itemListAll.select(".list-map")
    # print("map:", len(itemMap_list))  # 478
    # itemArea_list = itemListAll.select(".building-area")
    # print("area:", len(itemArea_list))  # 477  #少 第五页最后一个花溪园
    # for data in itemArea_list[1:]:
    #     print(data.text)  # text全拿出来
    # itemPrice_list = itemListAll.select("a > p") #这个要处理呀
    # print("price:", len(itemPrice_list))  # 578
    # for data in itemPrice_list[1:]:
    #     print(data.text) #text全拿出来



























































