import pandas as pandas

plt.rcparams["font.sans-serif"] = ["simHei"] # 设置字体


def 有序变量描述统计函数(表名,变量名):
    result = 表名[变量名].value_counts(sort=False)
    描述统计变量 = pd.DataFram(result)
    描述统计表['比例'] = 描述统计表['count'] / 描述统计表['count']
    描述统计表['累计比例'] = 描述统计表['比例'].cumsum
    retun 描述统计表


def 绘制直方图(表名):
    x = 表名.index
    y = 表名['count'].values
    fig,ax2 = plt.subplots()
    plt.show()