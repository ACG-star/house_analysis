from bs4 import BeautifulSoup
import re


def localData():
    print("正在提取数据......")
    with open(r'F:\PythonAnalysis\analysis item\Data\data\test.txt', 'rb') as fr:
        code = fr.read().decode("utf-8")
    return code


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
        # 小区名信息提取、清洗及取元素，以备存储使用
        nameList = item.find(attrs={"class": "items-name"}).text
        print(nameList)
        # print(name)#<span class="items-name">建业碧桂园龙悦城</span>
        # ruleName = re.compile('">(.*?)</')
        # nameInfos = re.findall(ruleName, str(nameList))
        # 新房宣传关键词
        # keyList = item.select(".tag")
        # ruleKey = re.compile('">(.*?)</')
        # keyInfos = re.findall(ruleKey, str(keyList))
        # for key in keyInfos:
        #     # 针对关键词后续做词云分析，因此单独保存一个文件，格式为txt
        #     with open(r"F:\关键词.txt", "a") as wt:
        #         wt.write(key + ' ')

if __name__ == '__main__':
    getData(localData())






















