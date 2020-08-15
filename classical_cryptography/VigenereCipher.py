import re

letterList = []     # 字母列表
# 初始化字母列表
for i in range(ord("a"), ord("z") + 1):
    letterList.append(chr(i))

# 加密
def encrypt():
    ciphertext = ""
    # 接收键入函数返回的列表
    massageAndKeyList = inputMassage()
    plaintextList = massageAndKeyList[0]
    keyList = massageAndKeyList[1]
    for i in range(len(plaintextList)):
        # 明文和密钥在表中的对应数值
        plaIndex = letterList.index(plaintextList[i])
        keyIndex = letterList.index(keyList[i % len(keyList)])
        # 做加法后区取余运算
        ciphertext += letterList[(plaIndex + keyIndex) % 26]
    return ciphertext

# 解密（加密的逆过程）
def decrypt():
    plaintext = ""
    # 接收键入函数返回的列表
    massageAndKeyList = inputMassage()
    ciphertextList = massageAndKeyList[0]
    keyList = massageAndKeyList[1]
    for i in range(len(ciphertextList)):
        # 密文和密钥在表中的对应数值
        cipIndex = letterList.index(ciphertextList[i])
        keyIndex = letterList.index(keyList[i % len(keyList)])
        # 取余运算
        plaintext += letterList[(cipIndex - keyIndex) % 26]
    return plaintext

# 键入
def inputMassage():
    massageList = []  # 消息序列
    keyList = []    # 密钥序列
    # 输入消息并创建消息序列
    massage = (re.sub("[^a-zA-Z]", "", input("Input text："))).lower()
    for i in massage:
        massageList.append(i)
    # 输入密钥并创建密钥序列
    key = (re.sub("[^a-zA-Z]", "", input("Input key："))).lower()
    for i in key:
        keyList.append(i)
    # 以列表形式返回输入的消息序列和密钥序列
    return [massageList, keyList]

if __name__ == "__main__":
    while True:
        print("——————维吉尼亚密码——————")
        print("1、Encrypt    2、Decrypt   3、Show Form")
        choice = int(input("Please choose（Input number）："))
        if choice == 1:
            ciphertext = encrypt()
            print("ciphertext：", ciphertext)
        elif choice == 2:
            plaintext = decrypt()
            print("plaintext：", plaintext)
        elif choice == 3:
            print("The Form Of This Operation：\n", letterList)
        else:
            print("Input error！")