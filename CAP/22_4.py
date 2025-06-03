import math
def main(n):
    if n == 0:
        return 0.14
    elif n == 1:
        return -0.79
    elif n>=2:
        return math.exp(main(n-1)) ** 3 + 1 + 31 * main(n-2) - 71

print(main(4))
print(main(5))
print(main(7))
print(main(3))
print(main(9))