#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 15:03
# @Author  : SystemDefenser
# @Email   : mrwx1116@163.com
# @Software: PyCharm

from random import randrange, shuffle

# 生成消息分组
def inputMassage(massage, keyLength):
    massageList = []
    # 扩充消息序列并创建分组
    while len(massage) % keyLength != 0:
        massage += " "
    for i in range(1, len(massage) + 1, keyLength):
        massageList.append(massage[i-1:i + keyLength - 1])
    return massageList

# 生成密钥
def createKey(keyLength):
    # 方法生成
    # keyList = [i for i in range(1, keyLength + 1)]
    # shuffle(keyList)    # 生成随机排序
    # 手工生成
    keyList = []
    while len(keyList) < keyLength:
        for i in range(1, keyLength + 1):
            key = randrange(1, keyLength + 1)
            if key not in keyList:
                keyList.append(key)
    return keyList

# 加密
def encrypt(massage, keyList):
    ciphertext = ""
    # 创建明文分组
    massageList = inputMassage(massage, keyLength)
    for item in massageList:
        # 存储改变字母位置后的临时列表
        itemList = [0 for i in range(len(keyList))]
        for i in range(len(keyList)):
            itemList[i] = list(item)[keyList[i] - 1]
            ciphertext += itemList[i]
    return ciphertext

# 解密
def decrypt(massage, keyList):
    plaintext = ""
    plaintextList = inputMassage(massage, keyLength)
    for item in plaintextList:
        # 存储改变字母位置后的临时列表
        itemList = [0 for i in range(len(keyList))]
        for i in range(len(keyList)):
            itemList[keyList[i] - 1] = list(item)[i]
        for i in itemList:
            plaintext += str(i)
    return plaintext

if __name__ == "__main__":
    while True:
        print("—————置换密码—————")
        choice = input("1、加密        2、解密\n请选择：")
        if choice == "1":
            massage = input("输入明文序列：")
            keyLength = int(input("输入分组长度："))
            keyList = createKey(keyLength)
            print("密钥分组：", keyList)
            ciphertext = encrypt(massage, keyList)
            print("密文结果：", ciphertext)
        elif choice == "2":
            massage = input("输入密文序列：")
            keyList = list(map(int, list(input("输入密钥序列：").split(","))))
            plaintext = decrypt(massage, keyList)
            print("明文：", plaintext)


