def normalMult(x, y, depth):
    lenY = len(y) 
    if depth == lenY:
        return 0
    lastDigit = y[lenY - 1 - depth]
    product = x * lastDigit * pow(10, depth)
    return product + normalMult(x, y, depth + 1)

def rectIntMult(x, y):
    lenX = len(x)
    lenY = len(y)
    if lenX == 1 or lenY == 1:
        return x[0] * y[0]
    maxLen = max(lenX, lenY)
    mid = maxLen//2
    a, b = x[:-mid], x[-mid:]
    c, d = y[:-mid], y[-mid:]
    sum = pow(10, maxLen) * rectIntMult(a, c) + pow(10, mid) * (rectIntMult(a, d) + rectIntMult(b, c)) + rectIntMult(b, d)
    return sum

def karatsubaMult(x, y):
    if x < 10 or y < 10:
        return x * y
    xStr = list(str(x))
    yStr = list(str(y))
    maxLen = max(len(xStr), len(yStr))
    mid = maxLen//2
    a, b = int(''.join(xStr[:-mid])), int(''.join(xStr[-mid:]))
    c, d = int(''.join(yStr[:-mid])), int(''.join(yStr[-mid:]))
    p = a + b
    q = c + d
    ac = karatsubaMult(a, c)
    bd = karatsubaMult(b, d)
    pq = karatsubaMult(p, q)
    adbc = pq - ac - bd
    sum = pow(10, 2 * mid) * ac + pow(10, mid) * adbc + bd
    return sum

num1Str = input("First number: ")
num2Str = input("Second number: ")
# num1Chars = list(num1Str)
# num2Chars = list(num2Str)
# num1Digits = list(map(int, num1Chars))
# num2Digits = list(map(int, num2Chars))
# sum = normalMult(int(num1Str), num2Digits, 0)
# sum = rectIntMult(num1Digits, num2Digits)
sum = karatsubaMult(int(num1Str), int(num2Str))
print(f'The result is: {sum}')
