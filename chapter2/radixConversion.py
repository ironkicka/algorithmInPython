n = 18

def convert(n,base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result

def convertToDecimalFromBinary(num):
    result = 0
    for i in range(len(num)):
        result += int(num[i]) * (2 ** (len(num) - i - 1))

    return(result)

print(convertToDecimalFromBinary('10010'))