# 安居客网站离线下载 7页 418条数据
import requests

def downloadData(url,i):
    # 添加headers信息，信息包括（操作系统信息NT，客户端(浏览器)信息），headers为字典格式，首尾不能存在空格
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
    }
    response = requests.get(url, headers=headers).text  #这里对request的结果使用text方法，获取源码
    with open(r'F:\PythonAnalysis\analysis item\Data\data\test{}.txt'.format(i), 'ab') as fw:  #使用aw都可  分割为多个文件 防止数据不纯粹 ab+/ab都会[当目录不存在时自动创建]
        fw.write(str(response).encode("utf-8")) #字符串编码解码，因此对源码类型转换为字符串
    print("开始写入……第{}页写入完成！".format(i))
    #分割多个文件存储原因：方便确定那一页数据未获取到或那一页被拦截，方便后续修改主函数组对具体页数重新获取

#主函数main
if __name__ == '__main__':
    for i in range(1, 8): #1-7
        i = str(i) #字符串拼接要求都是字符串类型
        baseurl = "https://ny.fang.anjuke.com/loupan/all/p"
        baseurl = baseurl + i + "/"
        downloadData(baseurl,i)
