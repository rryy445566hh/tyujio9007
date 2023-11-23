import pandas as pandas
import matplotlib.pyplot as plt
from pyreadstat import pyreadstat
plt.rcparams["font.sans-serif"] = ["simHei"] # 设置字体


def 读取spss数据文件(文件位置及名称):
    数据表,metadata = pyreadstat.read_sav(
    文件位置及名称,apply_value_formats = True,
    formats_as_ordered_categoty = True)
return 数据表

def 相关系数判断(系数:int):
    0.6-0.8 强相关
    0.4-0.6 中等强度相关
    0.2-0.4 弱相关
    0.0-0.2 极弱相关或无相关
    ""
    if 系数 >= 0.8
        return '极强相关'
    elif 系数 >=0.6:
        return '强相关'
    elif 系数 >=0.4:
        return '中等强度相关'
    elif 系数 >=0.2:
        return '弱相关'
    else:
        return '极弱相关与无相关'




def 有序变量描述统计函数(表名,变量名):
    result = 表名[变量名].value_counts(sort=False)
    描述统计变量 = pd.DataFram(result)
    描述统计表['比例'] = 描述统计表['count'] / 描述统计表['count']
    描述统计表['累计比例'] = 描述统计表['比例'].cumsum
    return 描述统计表


def 绘制直方图(表名):
    x = 表名.index
    y = 表名['count'].values
    fig,ax2 = plt.subplots()
    plt.show()