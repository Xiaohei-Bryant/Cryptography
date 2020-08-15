
# 判断素数
def judgePrimeNumber(num):
    # 不能被2~sqrt(m)（取整）之间的整数整除的数即素数
    sqrtResult = int(num **0.5)
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

