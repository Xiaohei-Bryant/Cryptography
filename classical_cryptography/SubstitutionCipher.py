import random, re

initialForm = []    # 初始字母表
resultForm = []     # 置换字母表
letterList = []     # 顺序字母列表

# 生成置换表
def creatForm():
    # 生成初始表格(A-Z)
    for i in range(ord("A"), ord("Z") + 1):
        initialForm.append(chr(i))
        letterList.append(chr(i + 32))

    # 生成置换表格(随机顺序)
    while len(resultForm) < 26:
        letter = random.choice(letterList)
        letterList.remove(letter)
        resultForm.append(letter)

# 加密
def encrypt(massage):
    ciphertext = ""
    for i in massage:
        ciphertext += resultForm[initialForm.index(i)]
    return ciphertext

# 解密
def decrypt(massage):
    plaintext = ""
    for i in massage:
        plaintext += initialForm[resultForm.index(i)]
    return plaintext

if __name__ == "__main__":
    creatForm()
    while True:
        print("——————代换密码——————")
        print("1、Encrypt    2、Decrypt   3、Show Form")
        choice = int(input("Please choose（Input number）："))
        if choice == 1:
            # 使用正则过滤非字母并转换为大写
            plaintext = (re.sub("[^a-zA-Z]", "", input("Input plaintext："))).upper()
            ciphertext = encrypt(plaintext)
            print("ciphertext：", ciphertext)
        elif choice == 2:
            # 使用正则过滤字母并转换为小写
            ciphertext = (re.sub("[^a-zA-Z]", "", input("Input ciphertext："))).lower()
            plaintext = decrypt(ciphertext)
            print("plaintext：", plaintext)
        elif choice == 3:
            print("The Form Of This Operation：\n", initialForm, "\n", resultForm)
        else:
            print("Input error！")
