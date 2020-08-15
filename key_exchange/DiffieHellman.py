#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 17:01
# @Author  : SystemDefenser
# @Email   : mrwx1116@163.com
# @Software: PyCharm

from random import randrange, choice

# 判断素数
def judgePrimeNumber(num):
    # 不能被2~sqrt(m)（取整）之间的整数整除的数即素数
    sqrtResult = int(num ** 0.5)
    for i in range(2, sqrtResult + 1):
        if num % i  == 0:
            return False
    return True

# 判断互质
def judgeCoPrime(a, b):
    # 求最大公因数
    def maxCommonFactor(m, n):
        result = 0
        while  m % n > 0:
            result = m % n
            m = n
            n = result
        return result
    if maxCommonFactor(a, b) == 1:
        return True
    return False

# 求所有本原根
def getPrimitiveRoot(primeNumber):
    primeList = []
    primitiveRootList = []
    # 求出所有互素元素
    for i in range(1, primeNumber):
        if judgeCoPrime(i, primeNumber):
            primeList.append(i)
    for i in primeList:
        tmpList = []
        for j in range(1, len(primeList) + 1):
            tmpList.append(i ** j % primeNumber)
        # 排序判断是否相同，相同则为
        tmpList.sort()
        if primeList == tmpList:
            primitiveRootList.append(i)
    return primitiveRootList

# 产生公钥
def createPubKey(primeNumber, primitiveRoot, randNum1, randNum2):
    pubKey1 = primitiveRoot ** randNum1 % primeNumber
    pubKey2 = primitiveRoot ** randNum2 % primeNumber
    return pubKey1, pubKey2

# 得到会话密钥
def createSubKey(primeNumber, pubKey1, pubKey2, randNum1, randNum2):
    subKey1 = pubKey2 ** randNum1 % primeNumber
    subKey2 = pubKey1 ** randNum2 % primeNumber
    return subKey1, subKey2

if __name__ == "__main__":
    print("—————Diffie-Hellman密钥交换—————")
    while True:
        primeNumber = int(input("输入共同素数："))
        if judgePrimeNumber(primeNumber):
            break
    # 两个随机数
    randNum1 = randrange(primeNumber)
    randNum2 = randrange(primeNumber)
    print("A随机数：", randNum1, "\nB随机数：", randNum2)
    # 挑选一个本原根
    primitiveRootList = getPrimitiveRoot(primeNumber)
    primitiveRoot = choice(primitiveRootList)
    print("所有本原根：", primitiveRootList)
    print("本次的本原根：", primitiveRoot)
    # 双方公钥和会话密钥
    pubKey1, pubKey2 = createPubKey(primeNumber, primitiveRoot, randNum1, randNum2)
    print("A公钥：", pubKey1, "\nB公钥：", pubKey2)
    subKey1, subKey2 = createSubKey(primeNumber, pubKey1, pubKey2, randNum1, randNum2)
    if subKey1 == subKey2:  # 必然成立
        print("AB共同会话密钥：", subKey1)
