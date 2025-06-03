import math

def main(z, x, y):
    a = math.sqrt((87*(38 * x ** 3 + y ** 2 / 41 + 1) ** 5 + 30 * z) / (69 * math.log(83 * x ** 2 - y) ** 7 - z))
    b = 46 * z ** 6 - 2 * math.exp(70 * x ** 2 - y - z ** 3 / 45) ** 5
    return a+b

print(main(-0.94, 0.92, -0.7))