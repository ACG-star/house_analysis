#房源信息需求分析：爬取房价、价格、地区、小区名。以csv格式保存
#信息来源-安居客：https://ny.fang.anjuke.com/loupan/all/
#反葛洪芳特训之”每个模糊的知识点都要有了解！！！“

#备注：
#使用面向对象方式编写
#由于网站频繁封禁反爬虫，所以采用手机热点dhcp动态分配ip迷惑反爬机制，好用度70%
#将数据下载至本地做离线处理 优点：防止频繁访问网站被反爬机制拦截封禁 缺点：数据更新不及时【但程序开发周期短，误差可忽略不计】

# 优化思路：
# 先给下载，然后离线处理
# 实现：两个方法/两个py文件
#
# 结构：[div class=item-mod]
#              [div class=infos]
#                   [a class=lp-name]
#                       [span class=items-name]         小区名
#                   [a class=address]
#                       [span class=list-map]           小区地址
#                   [a class=huxing]
#                       [span class=building-area]      建筑面积
#               [a class=favor-pos]
#                   [p class=price]
#                       [span]                          价格

# # 文件操作：
# import os
# #定义路径
# download = r"F:/test1/imgdir"
# #如果文件夹不存在则创建
# if not os.path.exists(download):
#     os.mkdir(download)
#     print("创建目录",download,"成功")
# print("下载路径:",download)

#开发日志：
#第一版处理地址信息，⬇则无需处理重复问题；第二版python分析数据
# 第一版不优化重复问题，数据分析使用excel；第二版实现列表去重，数据分析使用python实现；
#<!--王富贵-->



from bs4 import BeautifulSoup
import re
import csv

# 筛选、保存所需数据
def getData(code):  #传入形参

    print("开始处理......")
    # bs处理网页，方便以标签提取所需信息(!网页格式处理为二进制，.content)
    bs = BeautifulSoup(code,"html5lib")#安装解析库：pip install html5lib#升级pip：python -m pip install --upgrade pip
    #观察网页源码后发现所需信息位于许多个 [名为”infos“class选择器的div]和[class=price的p标签]
    # print(bs) #输出检测
    #查看源码 所需信息的位置 使用正则或bs提取

    itemListAll = bs.find_all("div", attrs={"class": "item-mod"})
    # print(type(itemListAll)) #bs4.element.ResultSet

    print("正在保存数据......")
    for item in itemListAll[1:]:
        # 因为csv写入时格式为列表嵌套，最终结果中列表格式[]无法去除，因此for循环嵌套取元素，最终写入

        # 新房宣传关键词
        keyList = item.select(".tag")
        ruleKey = re.compile('">(.*?)</')
        keyInfos = re.findall(ruleKey, str(keyList))
        for key in keyInfos:
            # 针对关键词后续做词云分析，因此单独保存一个文件，格式为txt
            with open(r"F:\PythonAnalysis\Data\data\关键词.txt", "a") as wt:
                wt.write(key + ' ')  #后续做词云分析分词处理需要拼接空格，这里直接拼接

        # 小区名信息提取、清洗及取元素，以备存储使用
        nameList = item.find(attrs={"class": "items-name"})
        # print(name)#<span class="items-name">建业碧桂园龙悦城</span>
        ruleName = re.compile('">(.*?)</')
        nameInfos = re.findall(ruleName, str(nameList))     #find 返回一个 -findall 返回全部
        for name in nameInfos:

            # 地址信息提取、清洗、二次清洗及取元素，以备存储使用
            addressList = item.select(".list-map")  # 包含所有地址信息的多个列表
            # print(address)#[<span class="list-map" target="_blank">[ 宛城区 宛城区 ] 雪枫路与仲景南路交叉口南侧</span>]
            ruleAddress = re.compile('">(.*?)</')  # 优化结束写个函数统一调用
            addressInfos = re.findall(ruleAddress, str(addressList).replace(u'\xa0', u'o_o'))  # 芜湖，nice
            # print(addressList)#['[\xa0宛城区\xa0宛城区\xa0]\xa0独山大道与光武路交会处西北角'] #\xa0 是不间断空白符 &nbsp;
            for addressData in addressInfos:
                #地址信息二次清洗
                # print(address)#[o宛城区o宛城区o]o雪枫路与仲景南路交叉口南侧
                ruleRegion = re.compile('o_o(.*?)o_o')  # region:行政区
                addressResult = re.search(ruleRegion, addressData)  # search 返回检索到的第一个结果 Result:结果
                address = addressResult.group(1)

                # 新房类型
                typeList = item.select(".wuyetp")
                ruleType = re.compile('">(.*?)</')
                typeInfos = re.findall(ruleType, str(typeList))
                for typ in typeInfos:

                    # 建筑面积提取、清洗及取元素，以备存储使用
                    areaList = item.select(".building-area")
                    ruleArea = re.compile('">(.*?)</span>')  # <span class="building-area">建筑面积：110-142㎡</span>
                    areaInfos = re.findall(ruleArea, str(areaList))
                    for area in areaInfos:

                        # 每平方价格信息提取、清洗及取元素，以备存储使用
                        priceList = item.select("a > p")
                        # print(price)
                        rulePrice = re.compile('<span>(.*?)</span>')
                        priceInfos = re.findall(rulePrice, str(priceList))
                        for price in priceInfos:

                            # 最终写入
                            with open(r"F:\PythonAnalysis\analysis item\Data\data\房源基础数据.csv", "a", newline="", encoding="utf-8") as f:
                                csvwrite = csv.writer(f)
                                csvwrite.writerow([name, address,typ, area, price])  # 写入时 格式必须为列表
                            with open(r"F:\PythonAnalysis\analysis item\Data\data\地址.txt", "a") as w:
                                w.write(address + ' ')
                            with open(r"F:\PythonAnalysis\analysis item\Data\data\类型.txt", "a") as w:
                                w.write(typ + ' ')
                            with open(r"F:\PythonAnalysis\analysis item\Data\data\面积.txt", "a") as w:
                                w.write(area + ' ')
                            with open(r"F:\PythonAnalysis\analysis item\Data\data\价格.txt", "a") as w:
                                w.write(price + ' ')

    print("处理完毕!")

#从本地提取合并后的数据
def localData():
    print("正在提取数据......")
    with open(r'F:\PythonAnalysis\analysis item\Data\data\test.txt', 'rb') as fr:
        code = fr.read().decode("utf-8")
    return code

# 合并原始数据
def merge():
    # 合并数据
    print("开始合并数据中……")
    with open(r'F:\PythonAnalysis\analysis item\Data\data\test.txt', 'ab') as fw:  # 合并必须用a ，另外这里不需要自己创建文件，如果不存在他会自己创建【文件操作见页首总备注】
        for i in range(1, 8):  #（1-7）
            with open(r'F:\PythonAnalysis\analysis item\Data\data\test{}.txt'.format(i), 'rb') as fri:
                data = fri.read().decode("utf-8")  # .read()方法读取所有行，将源码赋值给data utf-8解码【读取每个分割的text】
                fw.write(str(data).encode("utf-8"))  # 【合并每个texti到总text中】
                fri.close()
    print("数据合并完成！")

#主函数main
if __name__ == '__main__':
    #合并数据操作 只用一次即可
    # merge()
    # fileUrl = r"F:\Python price analysis\analysis item\Data\data"
    #准备csv文件,写入首行标题
    with open(r"F:\PythonAnalysis\analysis item\Data\data\房源基础数据.csv", "a", newline="", encoding="utf-8") as f:
        csvwrite = csv.writer(f)
        csvwrite.writerow(["小区名","地址","新房类型","建筑面积","每平方价格"])

    #引用函数,提取数据及存储
    getData(localData())  #传入实参

