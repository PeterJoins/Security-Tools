#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :2020/9/28
# @Author   :PeterJoin
#幂数加密

# a = open(r‘crypto11.txt‘,‘r‘)
# ciphertext = a.read()
ciphertext = "8842101220480224404014224202480122"

s = ciphertext.split('0')
flag = ''
for i in range(len(s)):
    list = []
    for j in s[i]:
        list.append(j)
    b = 0
    for k in list:
        b += int(k)
    # 字母ascii值与字母顺序相差为96
    flag += chr(b+96)
print("*"*25)
print('flag is ==>',flag)
