import pandas as pandas

plt.rcparams["font.sans-serif"] = ["simHei"] # ��������


def �����������ͳ�ƺ���(����,������):
    result = ����[������].value_counts(sort=False)
    ����ͳ�Ʊ��� = pd.DataFram(result)
    ����ͳ�Ʊ�['����'] = ����ͳ�Ʊ�['count'] / ����ͳ�Ʊ�['count']
    ����ͳ�Ʊ�['�ۼƱ���'] = ����ͳ�Ʊ�['����'].cumsum
    retun ����ͳ�Ʊ�


def ����ֱ��ͼ(����):
    x = ����.index
    y = ����['count'].values
    fig,ax2 = plt.subplots()
    plt.show()