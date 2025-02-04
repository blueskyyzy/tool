
"""
    百度翻译 单词
    author by blue
"""
import requests

url = 'https://fanyi.baidu.com/sug'
# url = 'https://fanyi.baidu.com/ait/text/translate'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'

}   # 处理一个小小的反爬
print("***********单词英汉双译已开启***********")
print("\n\t\t\t-------author by yzy")
resp = '1'
while True:
    s = input("\n\n\n请输入(t退出)：")
    if s == 't':
        break
    dat = {
        "kw": s
    }

    # 发送post请求, 发送的数据必须放到字典中, 通过data参数进行传递
    resp = requests.post(url, data=dat, headers=headers)

    # print(resp.json())

    my_list = resp.json()['data']
    print("")
    # for x in my_list[0]:
    #     print(f"{x}: {my_list[0][x]}")
    if my_list == []:
        print("\t无结果")
    i = 1
    for x in my_list:
        for y in x:
            if y == 'k':
                print("---------------------------")
            print(f"{y}{i}: {x[y]}")
        i += 1

resp.close()    # 关掉resp