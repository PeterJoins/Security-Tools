#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :2020/9/27
# @Author   :PeterJoin

import base64

a = open(r'/Users/peterjoin/Downloads/78697fd20e9c4ad295a62e5aa30ae052.txt','r')
s = a.read()

# base64解密一下
b = base64.b64decode(s).decode('ascii')
# 对解密后的字符串进行处理
b = b.strip('&#;')
c = []
c = b.split(';&#')
# unicode解密
d = ''
for i in c:
    d += chr(int(i))
# base64再次解密
e = base64.b64decode(d).decode('ascii')
# 对字符进行处理
e = e.strip('/')
f = []
f = e.split('/')
# 转化为ascii码
flag =''
for i in f:
    flag += chr(int(i))
print('flag is ',flag)