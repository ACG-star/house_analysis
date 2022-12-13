# 南阳市各区域间平均价格折线图+分析各区域内价格
#csv编码问题，用utf-8-sig格式：https://blog.csdn.net/qq_38882327/article/details/89637884；https://blog.csdn.net/mighty13/article/details/107132272/
# 区域和价格一一对照要求

import csv
import re

#从csv中提取数据
with open(r"F:\Python price analysis\analysis item\Data\data\房源基础数据.csv",encoding="utf-8-sig") as csvfile:
    #使用通用的utf-8编码时会出现{'\ufeff小区名': '建业碧桂园龙悦城', '地址': '高新区',……}
    # 这里出现的\ufeff是因为文本保存时包含了BOM（Byte Order Mark，字节顺序标记，出现在文本文件头部，Unicode编码标准中用于标识文件是采用哪种格式的编码）
    # 而导致的，解决方法是使用 utf-8-sig 编码
    reader = csv.DictReader(csvfile) #DictReader()方法的结果为  列名：值  的字典
    # print(reader)
    listAddress = []
    listPrice = []
    for row in reader:   #字典添加，结果为每项一个，值为最后添加的一个，因而不用
        listAddress.append(row['地址'])
        listPrice.append(row['每平方价格'])#创建一个地区 价格的列表，两者是一一对应的,然后写入字典进行同键求和
# print(listPrice)  #['8700', '11500', '6099', '11000', ……]
# print(listAddress) #['高新区', '宛城区', '卧龙区', '宛城区',……]
#['高新区', '宛城区', '卧龙区', '邓州', '西峡', '镇平', '方城', '淅川', '内乡', '新野', '南召', '社旗', '桐柏', '唐河', '其他地区']
dic = []
#列表推导式
dic = [x+'-'+y for x, y in zip(listAddress, listPrice)]  #['高新区-8700', '宛城区-11500', '卧龙区-6099', ……]

for r in dic:
    rule1 = re.compile('(.*?)-')
    rule2 = re.compile('-(.*?)')
    address = re.findall(rule1,r)
    print(address)
    if address =="高新区":
        price = re.findall(rule2, r)
        print(price)
    if address =="宛城区":
        price = re.findall(rule2, r)
        print(price)
    if address =="卧龙区":
        price = re.findall(rule2, r)
        print(price)
    if address =="邓州":
        price = re.findall(rule2, r)
        print(price)
    if address =="西峡":
        price = re.findall(rule2, r)
        print(price)
    if address =="镇平":
        price = re.findall(rule2, r)
        print(price)
    if address =="方城":
        price = re.findall(rule2, r)
        print(price)
    if address =="淅川":
        price = re.findall(rule2, r)
        print(price)
    if address =="内乡":
        price = re.findall(rule2, r)
        print(price)
    if address =="新野":
        price = re.findall(rule2, r)
        print(price)
    if address =="南召":
        price = re.findall(rule2, r)
        print(price)
    if address =="社旗":
        price = re.findall(rule2, r)
        print(price)
    if address =="桐柏":
        price = re.findall(rule2, r)
        print(price)
    if address =="唐河":
        price = re.findall(rule2, r)
        print(price)


















