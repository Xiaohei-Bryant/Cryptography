#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 15:25
# @Author  : SystemDefenser
# @Email   : mrwx1116@163.com
# @Software: PyCharm
from re import search

# 创建密钥流
def createKey(parameter, initialKey, keyLength):
    tmpKeyList = [] # 临时密钥序列（所有组合）
    cycleKeyList = []   # 周期密钥序列（末尾元素）
    resultKeyList = []  # 最终密钥序列（指定长度）
    parameterList = list(map(lambda x: int(x) - 1, list(parameter.split(" ")))) # 用于异或操作的位置
    tmpKeyList.append(list(map(lambda x: int(x), initialKey)))
    count = 0
    while True:
        # 存储每一轮的结果
        tmpList = [0 for i in range(len(initialKey))]
        tmpList[0] = tmpKeyList[count][int(parameterList[0])]
        # 依次异或
        for i in range(1, len(parameterList)):
            tmpList[0] ^= tmpKeyList[count][int(parameterList[i])]
        for i in range(1, len(initialKey)):
            tmpList[i] = tmpKeyList[count][i - 1]
        tmpKeyList.append(tmpList)
        count += 1
        if tmpKeyList[count] == tmpKeyList[0]:
            break
    print("=" * 50)
    print("周期：", len(tmpKeyList) - 1)
    # for item in tmpKeyList:
    #     print(tmpKeyList.index(item) + 1, item)
    for item in tmpKeyList[:-1]:
        cycleKeyList.append(item[-1])
    print("周期密钥：", cycleKeyList)
    print("周期：", len(cycleKeyList))
    for i in range(keyLength):
        resultKeyList.append(cycleKeyList[i % len(cycleKeyList)])
    print("加密密钥：", resultKeyList)
    print("长度：", len(resultKeyList))
    print("=" * 50)
    return resultKeyList

# 字符串转二进制
def strToBin(massage):
    resultStr = ""
    for i in massage:
        tmp = bin(ord(i)).replace("0b", "")
        while len(tmp) < 8:
            tmp = "0" + tmp
        resultStr += tmp
    return resultStr

# 二进制转字符串
def binToStr(massage):
    resultStr = ""
    for i in range(0, len(massage), 8):
        tmp = int(massage[i:i + 8], 2)
        resultStr += chr(tmp)
    return resultStr

# 加解密
def encrypt_decrypt(massage, keyList):
    resultStr = ""
    binStr = strToBin(massage)
    for i in range(len(binStr)):
        resultStr += str(int(list(binStr)[i]) ^ int(keyList[i % len(keyList)]))
    return resultStr

# 输入信息
def inputMassage():
    massage = input("输入Massage：")
    while True:
        initialKey = input("输入初始密钥（01串）：")
        if not search(r"[^0-1]", initialKey):
            break
    while True:
        parameter = input("输入反馈参数（空格隔开）：")
        parameterList = list(map(lambda x: int(x), list(parameter.split(" "))))
        if max(parameterList) <= len(initialKey):
            break
    keyLength = int(input("输入加密密钥长度："))
    # 返回初始消息（明文 / 密文）、初始密钥、反馈参数、加密密钥长度
    return massage, initialKey, parameter, keyLength

if __name__ == "__main__":
    while True:
        print("——————序列密码——————")
        choice = input("1、加密            2、解密\n请选择：")
        if choice == "1":
            massage, initialKey, parameter, keyLength = inputMassage()
            binStr = strToBin(massage)
            print("明文对应二进制序列：", binStr)
            keyList = createKey(parameter, initialKey, keyLength)
            cipherText_bin = encrypt_decrypt(massage, keyList)
            cipherText = binToStr(cipherText_bin)
            print("密文：", cipherText)
        elif choice == "2":
            massage, initialKey, parameter, keyLength = inputMassage()
            binStr = strToBin(massage)
            print("密文对应二进制序列：", binStr)
            keyList = createKey(parameter, initialKey, keyLength)
            cipherText_bin = encrypt_decrypt(massage, keyList)
            cipherText = binToStr(cipherText_bin)
            print("明文：", cipherText)
        else:
            continue