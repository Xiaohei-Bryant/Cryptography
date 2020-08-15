#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 14:53
# @Author  : SystemDefenser
# @Email   : mrwx1116@163.com
# @Software: PyCharm

from numpy import linalg

# 输入矩阵并判断是否存在逆矩阵
def inputMatrix():
    while True:
        # 输入一行、作为行列式的阶数和行列式的第一行
        rank = list(input("").split())
        matrix = [[0] * len(rank) for i in range(len(rank))]
        matrix[0] = rank
        # 输入行列式剩余数据
        for i in range(1, len(matrix)):
            matrix[i] = list(input("").split())
            # 判断每一行输入是否合法
            if len(matrix[i]) != len(matrix):
                print("输入有误，重新输入。")
                continue
        # 转换字符型为整型
        for i in range(len(matrix)):
            matrix[i] = list(map(lambda x: int(x), matrix[i]))
        # 判断是否存在逆矩阵
        if not judgeInverse(matrix):
            print("矩阵不存在逆矩阵，重新输入。")
            continue
        return matrix

# 判断是否存在逆元
def judgeInverse(matrix):
    try:
        linalg.inv(matrix)
    except:
        return False
    return True

# 生成密钥(矩阵的逆矩阵)
def createMatrixInverse(matrix):
    try:
        matrix_inverse = linalg.inv(matrix)
    except:
        return -1
    return matrix_inverse

# 生成消息分组
def createMassageList(massage, matrix):
    matrixRank = len(matrix)
    massageList = []
    # 扩充消息序列并创建分组
    while len(massage) % matrixRank != 0:
        massage += " "
    for i in range(1, len(massage) + 1, matrixRank):
        massageList.append(massage[i-1:i + matrixRank - 1])
    return massageList

# 字母序列转化为数字
def letterToDigit(massageList):
    massageDigitList = []  # 替换后的数字列表
    letterList = []  # 字母列表
    for i in range(ord("a"), ord("z") + 1):
        letterList.append(chr(i))
    for i in range(10):
        letterList.append(str(i))
    # 添加空格，解决分组填充问题
    letterList.append(" ")
    # 替换字母为数字
    for massage in massageList:
        listTmp = []
        for i in range(len(massage)):
            listTmp.append(letterList.index(massage[i]))
        massageDigitList.append(listTmp)
    return massageDigitList

# 数字序列转化为字母
def digitToLetter(massageList):
    massageLetterList = []  # 还原后的字母列表
    letterList = []
    for i in range(ord("a"), ord("z") + 1):
        letterList.append(chr(i))
    for i in range(10):
        letterList.append(str(i))
    letterList.append(" ")
    # 替换数字为字母
    for massage in massageList:
        massageLetterList.append(letterList[massage % 37])
    return massageLetterList

# 加密
def encrypt(massage, matrix):
    ciphertextList = [] # 加密结果列表
    massageList = createMassageList(massage, matrix)
    massageDigitList = letterToDigit(massageList)
    # 矩阵相乘
    for massageDigit in massageDigitList:
        for i in range(len(massageDigit)):
            sum = 0
            for j in range(len(massageDigit)):
                sum += massageDigit[j] * matrix[j][i % len(matrix)]
            ciphertextList.append(sum % 37)
    return ciphertextList

# 解密
def decrypt(massage, matrix):
    plaintextList = []  # 解密结果列表
    matrix_inverse = createMatrixInverse(matrix)
    massageList = createMassageList(massage, matrix)
    # 矩阵相乘
    for msg in massageList:
        for i in range(len(msg)):
            sum = 0
            for j in range(len(msg)):
                sum += msg[j] * matrix_inverse[j][i % len(matrix)]
            plaintextList.append(sum % 37)
    # 浮点型转换为整型(采用四舍五入——round())
    plaintextList = list(map(lambda x: int(round(x)), plaintextList))
    plaintextList = digitToLetter(plaintextList)    # 数字转换为字母
    plaintext = ""
    for item in plaintextList:
        plaintext += item
    return plaintext

if __name__ == "__main__":
    while True:
        print("—————希尔密码—————")
        choice = input("1、加密        2、解密\n请选择：")
        if choice == "1":
            print("输入矩阵：")
            matrix = inputMatrix()
            massage = input("输入msg：")
            massageList = createMassageList(massage, matrix)
            ciphertextList = encrypt(massage, matrix)
            print("加密结果：", ciphertextList)
        elif choice == "2":
            massageList = list(map(int, list(input("输入密文序列：").split(","))))
            print("输入矩阵：")
            matrix = inputMatrix()
            matrix_inverse = createMatrixInverse(matrix)
            print("逆矩阵：")
            for item in matrix_inverse:
                print(item)
            plaintext = decrypt(massageList, matrix)
            print("解密结果：", plaintext)
