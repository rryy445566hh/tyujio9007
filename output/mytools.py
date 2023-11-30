import pandas as pd
import matplotlib.pyplot as plt
from pyreadstat import pyreadstat
plt.rcParams["font.sans-serif"] = ["SimHei"]  # ��������

def ��ȡSPSS�����ļ�(�ļ�λ�ü�����, �Ƿ�����ǩֵ: bool):
    ���ݱ�, metadata = pyreadstat.read_sav(
        �ļ�λ�ü�����, apply_value_formats=�Ƿ�����ǩֵ, formats_as_ordered_category=True)
    return ���ݱ�


def ���ϵ���ж�(ϵ��: int):
    """
    �ж����ϵ����ǿ��

    """
    if ϵ�� >= 0.8:
        return '��ǿ���'
    elif ϵ�� >= 0.6:
        return 'ǿ���'
    elif ϵ�� >= 0.4:
        return '�е�ǿ�����'
    elif ϵ�� >= 0.2:
        return '�����'
    else:
        return '������ػ������'



def goodmanKruska_tau_y(df, x: str, y: str) -> float:
    """
    �����������������goodmanKruska_tau_y���ϵ��

    df:����������������ݿ�
    x:���ݿ�����Ϊ�Ա����Ķ����������
    y: ���ݿ�����Ϊ������Ķ����������

    ��������tau_y���ϵ��
    """

    cft = pd.crosstab(df[y], df[x], margins=True)
    """ ȡ��ȫ��������Ŀ """
    n = cft.at['All', 'All']
    """ ��ʼ������ """
    E_1 = E_2 = tau_y = 0

    """ ����E_1 """
    for i in range(cft.shape[0] - 1):
        F_y = cft['All'][i]
        E_1 += ((n - F_y) * F_y) / n
    """ ����E_2 """
    for j in range(cft.shape[1] - 1):
        for k in range(cft.shape[0] - 1):
            F_x = cft.iloc[cft.shape[0] - 1, j]
            f = cft.iloc[k, j]
            E_2 += ((F_x - f) * f) / F_x
    """ ����tauy """
    tau_y = (E_1 - E_2) / E_1

    return tau_y

def �����������ͳ�ƺ���(����, ������):
    result = ����[������].value_counts(sort=False)
    ����ͳ�Ʊ� = pd.DataFrame(result)
    ����ͳ�Ʊ�['����'] = ����ͳ�Ʊ�['count'] / ����ͳ�Ʊ�['count'].sum()
    ����ͳ�Ʊ�['�ۼƱ���'] = ����ͳ�Ʊ�['����'].cumsum()
    return ����ͳ�Ʊ�


    def ����ֱ��ͼ(����):
    x = ����.index
    y = ����['count'].values
    fig, ax2 = plt.subplots()
    ax2.bar(x, y)
    plt.show()