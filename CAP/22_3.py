import math

def main(n ,m, a):
    total = 0
    for k in range(1, a + 1):
        inner_sum = 0
        for c in range(1, m + 1):
            inner_sum2 = 1
            for j in range(1, n + 1):
                inner_sum2 *= ((j ** 2 / 91) - 51 * math.floor(j + (91 * (k ** 3)) + (c ** 2)))
            inner_sum += inner_sum2
        total += inner_sum

    return total

print(main(5, 8, 5))