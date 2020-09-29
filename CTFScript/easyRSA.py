#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gmpy2

p = 473398607161   #pq 为两个不同的大素数
q = 4511491
e = 17            #1-s 之间随机选择一个整数

s = (p-1)*(q-1)      # N=pq为密钥长度，S为N的欧拉函数
d = gmpy2.invert(e,s)    #d 为e对s的模反元素，用扩展欧几里得算法求解。公钥P=（e,N），私钥S=（d,N）
print("*"*25)
print('flag is :',d)