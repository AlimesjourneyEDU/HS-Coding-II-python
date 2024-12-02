
def countDigits(num):
    num = abs(num)
    digitCount = 0
    while num != 0:
        num //= 10
        digitCount += 1
    return digitCount


n1 = int(input("ur Number?"))


print(f"there are {countDigits(n1)} numbers in {n1}")