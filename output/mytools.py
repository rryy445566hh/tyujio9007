import pandas as pandas
import matplotlib.pyplot as plt
plt.rcparams["font.sans-serif"] = ["simHei"] # ��������


def �����������ͳ�ƺ���(����,������):
    result = ����[������].value_counts(sort=False)
    ����ͳ�Ʊ��� = pd.DataFram(result)
    ����ͳ�Ʊ�['����'] = ����ͳ�Ʊ�['count'] / ����ͳ�Ʊ�['count']
    ����ͳ�Ʊ�['�ۼƱ���'] = ����ͳ�Ʊ�['����'].cumsum
    return ����ͳ�Ʊ�


def ����ֱ��ͼ(����):
    x = ����.index
    y = ����['count'].values
    fig,ax2 = plt.subplots()
    plt.show()