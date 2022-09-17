import requests
import json
import time
import os
import sys
from colorama import init
init(autoreset=True)

localtime = time.asctime(time.localtime(time.time()))


def translate(url, data, headers):
    response = requests.post(url=url, data=data, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        dic_obj = response.json()
        # with open('data.json', 'w', encoding='utf-8') as fp:
        #     fp.write(json.dumps(dic_obj, ensure_ascii=False, indent=2))
        if (dic_obj['errno'] == 0):
            if dic_obj['data'] == []:
                print("\033[32m"+localtime+"\033[0m", '：输入错误！')
                return 0, 0
            else:
                for i in range(0, len(dic_obj['data'])):
                    # print(len(dic_obj['data']))
                    print("\033[32m" + dic_obj['data']
                          [i]['k']+"\033[0m", end='')
                    print(": ""\033[33m" + dic_obj['data'][i]['v']+"\033[0m")
                    # word = str(dic_obj['data'][i]['k'])
                    # translate = str(dic_obj['data'][i]['v'])
        else:
            print(dic_obj['errmsg'])
    else:
        print("\033[32m"+localtime+"\033[0m", "：请求失败，错误码: " + status_code)


if __name__ == "__main__":
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.33'
    }
    print(
        "\033[1;31;40mtranslate:\033[0m Welcome to translate! Enter h to get help.")
    print("\033[1;31;40mtranslate:\033[0m\033[33m "+localtime+"\033[0m")
    print("\033[1;31;40mtranslate:\033[0m 终端翻译软件")
    print("\033[1;31;40mtranslate:\033[0m 开发者：@k1d3")
    print("\033[1;31;40mtranslate:\033[0m 本程序为开源程序，遵循GPL-3.0协议")
    print("--------------------------------------------------")

    while 1:
        while 1:
            print("\033[1;31;40mtranslate>\033[0m", end='')
            word = input()
            if word == '':
                print("\033[32m"+localtime+"\033[0m", "：输入为空！请重新输入！")
            elif word == 'q':
                print("\033[32m"+localtime+"\033[0m" "：退出成功！")
                sys.exit()
            elif word == 'cls':
                os.system('cls')
            elif word == 'h':
                print("：帮助：\n\tq: 退出程序\n\tcls: 清屏\n\th: 帮助")
            else:
                break
        data = {
            'kw': word
        }
        translate(url, data, headers)
        # (word_, translate_) = translate(url, data, headers)
        # if word_ == 0:
        # continue
        # db = mysql.connect()
        # cursor = db.cursor()
        # mysql.isEmpty(cursor)
        # mysql.insert(cursor, word_, translate_)
        # db.close()
