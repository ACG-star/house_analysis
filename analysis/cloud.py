#房源数据分析：
# 南阳市新房类型饼图  √
# 新房宣传词词云    √
# 南阳市各区域间平均价格折线图+分析各区域内价格
# 南阳新房价格箱线图  【待定】  【不做】
# 建筑面积条形图  √

#开发日志：
#安装词云库失败的vc问题⬇下载链接
# https://download.visualstudio.microsoft.com/download/pr/7b196ac4-65a9-4fde-b720-09b5339dbaba/78df39539625fa4e6c781c6a2aca7b4f/vs_community.exe
#scipy库使用详解：
# https://blog.csdn.net/RosebudTT/article/details/105979939?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164515973416780269812593%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164515973416780269812593&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-105979939.pc_search_result_positive&utm_term=scipy&spm=1018.2226.3001.4187
#from scipy.misc import imread      scipy.misc模块 scipy库的杂项模块，其中包含绘制轮廓函数imread(),详见⬇:
# https://blog.csdn.net/baishuo8/article/details/89842215
#img类型转换原因
# https://blog.csdn.net/HaoZiHuang/article/details/105798801
#wordclou用法：
# https://blog.csdn.net/weixin_39604598/article/details/110463986

from wordcloud import WordCloud        #安装时可能缺少vc++开发环境，详见开发日志
import imageio    #背景轮廓图片
import matplotlib.pyplot as mplt


def img_grearte():
    img = imageio.imread("house.png")
    with open(r"F:\PythonAnalysis\analysis item\Data\data\关键词.txt", "r") as f:  # 读取待处理文本 文本已空格分隔 无需处理
        txt = f.read()
    #设置生成的词云参数
    wc = WordCloud(background_color="white",
                     width=800,
                     height=800,
                     font_path=r'E:/pycharm/font/simsun.ttc', #中文字库，wordcloud默认字体是不支持中文
                     mask=img,)
    wcloud = wc.generate(txt)  #传入数据
    wcloud.to_file(r'F:\PythonAnalysis\analysis item\Data\data\wordcloud.png') #保存到本地
    print("词云图片已保存")

    mplt.imshow(wcloud)  # 使用plt库显示图片
    mplt.axis("off")   # 矩形图表区域内不显示xy轴
    mplt.show()




if __name__ == '__main__':
    img_grearte()


