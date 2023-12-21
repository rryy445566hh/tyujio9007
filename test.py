import SparkApi
# ������Կ��Ϣ�ӿ���̨��ȡ
appid = "508e778e"  # ��д����̨�л�ȡ�� APPID ��Ϣ
api_secret = ""  # ��д����̨�л�ȡ�� APISecret ��Ϣ
api_key = ""  # ��д����̨�л�ȡ�� APIKey ��Ϣ

# �������ô�ģ�Ͱ汾��Ĭ�ϡ�general/generalv2��
domain = "generalv3"   # v1.5�汾
# domain = "generalv2"    # v2.0�汾
# �ƶ˻����ķ����ַ
Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"  # v1.5�����ĵ�ַ
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0�����ĵ�ַ


text = []

# length = 0


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


if __name__ == '__main__':
    text.clear
    while (1):
        Input = input("\n" + "��:")
        question = checklen(getText("user", Input))
        SparkApi.answer = ""
        print("�ǻ�:", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi.answer)
        # print(str(text))