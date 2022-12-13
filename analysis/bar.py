#建筑面积条形图

import re
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']    #解决不能显示中文的问题

#从本地取原始数据
txt = open(r"F:\PythonAnalysis\analysis item\Data\data\面积.txt", "r").read()
# print(txt)
#使用正则只获取面积数据
rule1 = re.compile('-(.*?)㎡')
area = re.findall(rule1,txt)
#建筑面积：410-1030㎡ 建筑面积：87000㎡ 建筑面积：500000㎡ 建筑面积：347794㎡ 建筑面积：37-147.65㎡
#利用正则剔除万级别的非法数据 利用追加剔除千级别的非法数据
# print(area)
#剔除不合法数据 将合法数据追加于新列表中 append方法无返回值，直接修改原来的列表。
listData = []
for i in area:
    # 因为存在小数点，所以用小数格式判断，意为以10为基数的int类型，对128.69文本无效
    # 否则报值错误【ValueError: invalid literal for int() with base 10: '128.69'】
    if float(i) < 1000:
        listData.append(i)
# print(listData) #len(listData) 419

#划分面积区间
#A   <=70 1-2人
#B   <=100 2-3人
#C   <=130 3-5人
#D   >130  大型房屋
one = []
two = []
three = []
four = []
for i in listData:
    if float(i) <= 70:
        one.append(i)
    elif float(i) <= 120:
        two.append(i)
    elif float(i) <= 150:
        three.append(i)
    else:
        four.append(i)
a = len(one)
b = len(two)
c = len(three)
d = len(four)
print(a,b,c,d)  #5 18 87 309
x = ['0-70㎡','70.1-120㎡','120.1-150㎡','150+㎡']
num = [a,b,c,d] #5 36 256 122

plt.bar(x=x,height=num)
plt.title('南阳地区新房建筑面积条形图')
plt.show()












#对建筑面积取平均值的失败尝试：问题在于建筑面积信息部分格式不统一，目前无法准确获取每个部分的最大最小值，因而导致失败。

# #使用正则只获取面积数据
# ruleMax = re.compile('-(.*?)㎡')
# ruleMin = re.compile('：(.*?)-') #注意是中文冒号
# areaMax = re.findall(ruleMax,txt)
# areaMin= re.findall(ruleMin,txt) #建筑面积：55519㎡
# # print(len(areaMax))
# # print(len(areaMin))  #421
# #建筑面积：410-1030㎡ 建筑面积：87000㎡ 建筑面积：500000㎡ 建筑面积：347794㎡ 建筑面积：37-147.65㎡
# #利用正则剔除万级别的非法数据 利用追加剔除千级别的非法数据
# # print(area)
# #剔除不合法数据 将合法数据追加于新列表中 append方法无返回值，直接修改原来的列表。
# print(areaMax)
# print(areaMin)
#
# '1111110㎡ 建筑面积：243914㎡ 建筑面积：190762㎡ 建筑面积：243914㎡ 建筑面积：27000㎡ 建筑面积：119.99',
# #首先类型转换为浮点型（因为存在小数），方便后续取平均运算 用列表推导式
# areaMax = [float(i) for i in areaMax]
# areaMin = [float(i) for i in areaMin]
# #最大最小取中间 在zip函数格式中直接对应相加除以二 取平均
# area = [(x+y)/2 for x, y in zip(areaMax, areaMin)]  #格式：[运算 for 一一对应 in zip(列表1，列表2)] 又名列表推导式
# #格式解释 []表明结果生成的是列表  推导式：运算要求 for 运算元素1，元素2 in zip（列表1，列表2）
# #zip函数将多个列表视为一个整体，遍历时，同时从各个列表里取出相同索引位置的元素，列表元素一一对应
# #注意：列表长度相同；列表里的元素都是int类型数据；对应索引位置元素相加，生成新的列表
# print(area)


