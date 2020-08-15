
# 创建字母表
def creatLetterList():
    letterList = []
    for i in range(ord("a"), ord("z") + 1):
        letterList.append(chr(i))
    # 添加数字0—9
    for i in range(10):
        letterList.append(str(i))
    return letterList

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

# 求逆元
def getInverse(a, b):
    # 扩展的欧几里得
    def extGcd(a_, b_, arr):
        if b_ == 0:
            arr[0] = 1
            arr[1] = 0
            return a_
        g = extGcd(b_, a_ % b_, arr)
        t = arr[0]
        arr[0] = arr[1]
        arr[1] = t - int(a_ / b_) * arr[1]
        return g
    # 求a模b的乘法逆x
    arr = [0,1,]
    gcd = extGcd(a, b, arr)
    if gcd == 1:
        return (arr[0] % b + b) % b
    else:
        return -1

# 加密
def encrypt(massage, keyOne, keyTwo):
    massageList = []     # 存储明文字母转换的对应数字
    cipherTextList = []  # 密文列表
    letterList = creatLetterList()  # 字母列表
    for i in massage:
        massageList.append(letterList.index(i))
    for i in massageList:
        cipherTextList.append((keyOne * i + keyTwo) % len(letterList))
    return cipherTextList

# 解密
def decrypt(cipherTextList, keyOne, keyTwo):
    plainTextList = []
    letterList = creatLetterList()
    # 求keyOne对于26的逆元
    inverse_keyOne = getInverse(keyOne, len(letterList))
    for i in cipherTextList:
        plainTextList.append((inverse_keyOne * (i - keyTwo)) % len(letterList))
    for i in range(len(plainTextList)):
        plainTextList[i] = letterList[plainTextList[i]]
    # 将列表整合为字符串
    plianText = "".join(plainTextList)
    return plianText

# 输入并创建密钥
def creatKey():
    while True:
        keyOne = int(input("输入Key1（与36互质）："))
        if not judgeCoPrime(keyOne, 36):
            continue
        keyTwo = int(input("输入Key2："))
        break
    # 创建keyOne的逆元
    inverse_keyOne = getInverse(keyOne, 36)
    return keyOne, keyTwo, inverse_keyOne

if __name__ == "__main__":
    while True:
        print("——————仿射密码——————")
        choice = input("1、加密    2、解密\n请选择：")
        if choice == "1":
            keyOne, keyTwo, inverse_keyOne = creatKey()
            print("创建密钥成功：<K1：%d> <K2：%d> <K1逆元：%d>" %(keyOne, keyTwo, inverse_keyOne))
            massage = input("输入明文：")
            cipherTextList = encrypt(massage, keyOne, keyTwo)
            print("加密结果：", cipherTextList)
        elif choice == "2":
            cipherTextList = list(map(int, list(input("输入密文序列：").split(","))))
            keyOne, keyTwo, inverse_keyOne = creatKey()
            plainText = decrypt(cipherTextList, keyOne, keyTwo)
            print("解密结果：", plainText)
        else:
            continue