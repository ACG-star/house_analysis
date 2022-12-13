#房屋类型饼图
#pip升级python -m pip install --upgrade pip
#安装jieba库：pip install jieba
#python词频统计 ：https://www.cnblogs.com/wkfvawl/p/9487165.html
## 使用结巴默认分词结果不尽人意：{'住宅': 434, '商住': 28, '临街': 10, '店铺': 10, '标准': 1, '写字楼': 1, '别墅': 4}
# 因此使用自定义分词：参考网址：https://www.cnblogs.com/yoyowin/p/12856964.html
# 这里使用临时分词 即jieba.add_word(词,词性代码)
import jieba
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']    #解决不能显示中文的问题
#绘图默认不显示中文 通过参数字典 rcParams 修改已经加载的配置项，sans-serif 表示字体中的无衬线体，SimHe 是 黑体
# 这里参考https://blog.csdn.net/weixin_39524882/article/details/109969400和https://www.cnblogs.com/shanger/p/13021452.html


##############################住宅类型饼图#########################################

#获取类型源数据
txt = open(r"F:\PythonAnalysis\analysis item\Data\data\类型.txt", "r").read()
jieba.add_word('临街店铺')   #添加两个临时分词规则 词性代码使用默认即可
jieba.add_word('标准写字楼')
words = jieba.lcut(txt)

dic = {}   #定义一个空字典，用于词频键值对  {键:值}   {住宅：次数}
for word in words:
    if len(word) == 1:    # 单个词语不计算在内 剔除文本中的‘ ’分割符
        continue
    else:
        # 遍历所有词语，每出现一次其对应的值加 1
        dic[word] = dic.get(word, 0) + 1    #dict.get(word,0)获取字典对应键的值，如果不存在则返回0 存在则+1
# print(dic)  map（）。reduce（）+1

#分离键值，用于做绘图数据准备
typNmae = list(dic.keys())
# print(typNmae)   #['住宅', '商住', '临街店铺', '标准写字楼', '别墅']
typValue = list(dic.values())
# print(typValue)   #[434, 28, 10, 1, 4]

separate = (0.1,0.1,0.1,0.4,0.1)  #分离比
plt.pie(x=typValue, labels=typNmae, explode=separate, autopct='%.1f%%')
#autopct 显示数值标签，以百分比格式显示 精度为精确百分号后一位 末尾用%%转义显示%
#添加图形标题
plt.title('南阳地区新房类型饼图')
plt.show()


######################################新房所在区域占比及条形图######################################
#获取源数据
address = open(r"F:\PythonAnalysis\analysis item\Data\data\地址.txt", "r").read()
# print(address)
words = jieba.cut(address,cut_all=False) #jieba的精确模式，会尽可能少的进行分词，尽可能多的合并词语
jieba.add_word('官庄工区')
jieba.add_word('南阳周边')
jieba.add_word('鸭河工区')
dic = {}   #定义一个空字典，用于词频键值对
for word in words:
    if len(word) == 1:    # 单个词语不计算在内 剔除文本中的‘ ’分割符
        continue
    else:
        # 遍历所有词语，每出现一次其对应的值加 1
        dic[word] = dic.get(word, 0) + 1    #dict.get(word,0):获取字典对应键的值，如果不存在则返回0 存在则+1 结果作为value赋值给key
# print(dic) #'官庄工区': 1, '南阳周边': 1, '鸭河工区': 1 #将后三个合并为其他地区
del dic['官庄工区']
del dic['南阳周边']
del dic['鸭河工区']
#向字典添加 ’其他‘：3
dic['其他地区'] =3
# print(dic)
# #{'高新区': 19, '宛城区': 112, '卧龙区': 70, '邓州': 69, '西峡': 18, '镇平': 33, '方城': 34, '淅川': 11, '内乡': 20, '新野': 30, '南召': 15, '社旗': 25, '桐柏': 4, '唐河': 14, '其他地区': 3}

#分离键值，用于做绘图数据准备
typNmae = list(dic.keys())
# print(typNmae)   #['高新区', '宛城区', '卧龙区', '邓州', '西峡', '镇平', '方城', '淅川', '内乡', '新野', '南召', '社旗', '桐柏', '唐河', '其他地区']
typValue = list(dic.values())
# print(typValue)   #[19, 112, 70, 69, 18, 33, 34, 11, 20, 30, 15, 25, 4, 14, 3]

separate = (0.1,0,0,0,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)  #分离比 一个元素一个数
plt.pie(x=typValue, labels=typNmae, explode=separate,autopct='%.1f%%')
#autopct 显示数值标签，以百分比格式显示 精度为精确百分号后一位 末尾用%%转义显示%
#添加图形标题
plt.title('新房区域占比饼图')
plt.show()

#同数据条形图
fig = plt.figure(figsize = (10,5))  #调整默认绘图区域大小，因为会出现横坐标重叠的问题
plt.bar(x=typNmae,height=typValue,alpha = 1)
#间距：alpha = 0.8  范围为（0-1）
#画布大小：figsize提供整数元组则会以该元组为长宽，单位是英寸
plt.title('新房区域数量条形图')
plt.show()

















