import pandas as pandas
import matplotlib.pyplot as plt
from pyreadstat import pyreadstat
plt.rcparams["font.sans-serif"] = ["simHei"] # ��������


def ��ȡspss�����ļ�(�ļ�λ�ü�����):
    ���ݱ�,metadata = pyreadstat.read_sav(
    �ļ�λ�ü�����,apply_value_formats = True,
    formats_as_ordered_categoty = True)
return ���ݱ�

def ���ϵ���ж�(ϵ��:int):
    0.6-0.8 ǿ���
    0.4-0.6 �е�ǿ�����
    0.2-0.4 �����
    0.0-0.2 ������ػ������
    ""
    if ϵ�� >= 0.8
        return '��ǿ���'
    elif ϵ�� >=0.6:
        return 'ǿ���'
    elif ϵ�� >=0.4:
        return '�е�ǿ�����'
    elif ϵ�� >=0.2:
        return '�����'
    else:
        return '��������������'




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