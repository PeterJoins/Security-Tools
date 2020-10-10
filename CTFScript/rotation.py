#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :2020/9/28
# @Author   :PeterJoin

rotor = [
    "ZWAXJGDLUBVIQHKYPNTCRMOSFE", "KPBELNACZDTRXMJQOYHGVSFUWI", 
    "BDMAIZVRNSJUWFHTEQGYXPLOCK", "RPLNDVHGFCUKTEBSXQYIZMJWAO", 
    "IHFRLABEUOTSGJVDKCPMNZQWXY", "AMKGHIWPNYCJBFZDRUSLOQXVET", 
    "GWTHSPYBXIZULVKMRAFDCEONJQ", "NOZUTWDCVRJLXKISEFAPMYGHBQ", 
    "XPLTDSRFHENYVUBMCQWAOIKZGJ", "UDNAJFBOWTGVRSCZQKELMXYIHP", 
    "MNBVCXZQWERTPOIUYALSKDJFHG", "LVNCMXZPQOWEIURYTASBKJDFHG", 
    "JZQAWSXCDERFVBGTYHNUMKILOP" 
]
 
cipher = "NFQKSEVOQOFNP"
 
key = [2,3,7,5,13,12,9,1,8,10,4,11,6]
 
tmp_list=[]
 
for i in range(0, len(rotor)):
    tmp=""
    k = key[i] - 1
    for j in range(0, len(rotor[k])):
        if cipher[i] == rotor[k][j]:
            if j == 0:
                tmp=rotor[k]
                break
            else:
                tmp=rotor[k][j:] + rotor[k][0:j]
                break
    tmp_list.append(tmp)
# print(tmp_list)
 
message_list = []
for i in range(0, len(tmp_list[i])):
    tmp = ""
    for j in range(0, len(tmp_list)):
        tmp += tmp_list[j][i]
    message_list.append(tmp)
 
print(message_list)


def spread_list(lst):
    for item in lst:
        if isinstance(item,(list,tuple)):
            yield from spread_list(item)
        else:
            yield item
        pass
def banner():
    print(("""%s
  __  _   __    _____    __  _   __           __      __ _____ 
  \_\/ | / /__ / ___ \   \_\/ | / /__ _____  (())    (())_____|
 / _ \ |/ /_  ) | _ \ \ / _ \ |/ /_  )___  |/ _ '|  / _ '|     
|  __/_/ / / /  |   /  |  __/_/ / / /    |_| (_| | | (_| |     
 \___|/_/ /___\ |_|_\ / \___|/_/ /___|      \__,_|  \__,_|     
               \_____/                                         
                                                               %s%s
        # Coded By PeterJoin -托马斯杰斐逊 转轮加密（´・ω・）
        # https://github.com/PeterJoins/Security-Tools/blob/master/CTFScript/rotation.py %s
    """ % ('\033[91m', '\033[0m', '\033[93m', '\033[0m')))

if __name__ == '__main__':
    banner()
    for i in spread_list(message_list):
        print("*"*25)
        print(i.lower())