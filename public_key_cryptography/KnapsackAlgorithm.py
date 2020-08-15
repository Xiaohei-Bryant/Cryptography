import random
from my_modules import modules

# 初始化
def init(length, interval):
    listV = []  # 超递增向量
    listV_b = []  # 每个元素对应的乘数
    bagCapacity = 1000  # 背包容积
    # 初始化超递增向量与listV_b
    for i in range(length):
        listV.append(sum(listV) + random.randrange(1, interval))
        listV_b.append(0)
    # 求超递增背包的解
    bagCapacityTmp = bagCapacity
    for i in range(len(listV)-1, -1, -1):
        if bagCapacityTmp >= listV[i]:
            bagCapacityTmp -= listV[i]
            listV_b[i] = 1
    return listV

# 产生私钥：k、t、t的逆元
def creatPKey(listV):
    # listV = init()
    while True:
        k = int(input("输入私钥k(大于%d)：" % (sum(listV))))
        if k <= sum(listV):
            continue
        while True:
            t = int(input("输入私钥t(与k互素)："))
            if not modules.judgeCoPrime(k, t):
                continue
            break
        break
    inverse_t = modules.getInverse(t, k)
    return k, t, inverse_t

# 产生公钥：
def creatSKey(listV, t, k):
    sKeyList = [] # 公钥序列
    for i in listV:
        sKeyList.append(i * t % k)
    return sKeyList

# 加密
def encrypt(massage, sKeyList):
    massageList = []    # 明文分组后的列表
    ciphertextList = [] # 存储密文的列表
    # 扩充明文消息串
    while len(massage) % len(sKeyList) != 0:
        massage = "0" + massage
    # 对明文进行分组
    for i in range(int(len(massage) / len(sKeyList))):
        start = (i * len(sKeyList))
        end = ((i + 1) * len(sKeyList))
        massageList.append(massage[start : end])
    # 采用内积和的方法加密
    for i in massageList:
        # 此处使用lambda时，要注意类型转换
        multiplyList = list(map(lambda x, y: int(x) * int(y), list(i), sKeyList))
        ciphertextList.append(sum(multiplyList))
    return ciphertextList

# 解密
def decrypt(massage, sKeyList, k, inverse_t):
    plaintextList = [] # 存储明文的列表
    reductListV = []  # 还原后的初始超递增向量
    # 还原超递增向量
    for i in sKeyList:
        reductListV.append(int(i) * inverse_t % k)
    # 计算出用于解密的临时背包容积
    bagCapacityList = []
    for i in massage:
        bagCapacityList.append(int(i) * inverse_t % k)
    # 利用求出的临时背包容积求解背包问题，结果即明文
    for bagCap in bagCapacityList:
        plaintextTmp = []   # 存储密文列表中每个密文解密后的序列
        for i in range(len(reductListV)):
            plaintextTmp.append(0)
        for i in range(len(reductListV) - 1, -1, -1):
            if bagCap >= reductListV[i]:
                bagCap -= reductListV[i]
                plaintextTmp[i] = 1
        plaintextList += plaintextTmp
    # 去除扩充的0并转换为字符串
    start, end = 0, 0
    for i in range(len(plaintextList)):
        if plaintextList[i] != 0:
            break
        end = i + 1
    del plaintextList[start : end]
    plaintextList = map(str, plaintextList)
    plaintext = "".join(plaintextList)
    return plaintext

if __name__ == "__main__":
    print("——————背包算法（公钥密码）——————")
    # listV = [1, 3, 7, 13, 26, 65, 119, 267]
    length = int(input("输入超递增向量元素个数："))
    interval = int(input("输入随机增量最大值："))
    # length, interval = 8, 4
    listV = init(length, interval)
    print("初始向量：", listV)
    k, t, inverse_t = creatPKey(listV)
    print("\n私钥验证成功，分别为  <k：%d>， <t：%d>，<t逆元：%d>" %(k, t, inverse_t))
    sKeyList = creatSKey(listV, t, k)
    print("公钥向量为：", sKeyList, "\n")
    while True:
        choice = input("1、加密    2、解密\n请选择：")
        if choice == "1":
            massage = input("输入明文（01序列）：")
            ciphertextList = encrypt(massage, sKeyList)
            print("加密结果：", ciphertextList)
        elif choice == "2":
            ciphertextList = list(map(int, list(input("输入密文：").split(","))))
            sKeyList = list(map(int, list(input("输入公钥向量：").split(","))))
            k = int(input("输入密钥k："))
            inverse_t = int(input("输入密钥t逆："))
            plaintext = decrypt(ciphertextList, sKeyList, k, inverse_t)
            print("解密结果：", plaintext)
