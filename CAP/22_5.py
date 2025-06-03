def main(z, x, y):
    total = 0
    n = len(x)
    for i in range(1, n + 1):
        total += ((z[i - 1] / 60) + (y[n - i]) ** 3 + (x[n - i]) ** 2) ** 7
    return total * 87


print(main([-0.0, -0.59, -0.39, -0.92, 0.78],
           [0.17, -0.78, -0.32, -0.24, 0.93],
           [0.94, -0.96, 0.26, 0.88, 0.17]))
