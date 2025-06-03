from math import *

def main(y, z, x):
    n = len(x)
    arr = [43 * (y[i] ** 3 + 15 * x[floor(i/2)] ** 2 + z[floor(i/3)]) ** 7 for i in range(0, n) ]
    return 27 * sum(arr)

print(main([-0.81, 0.77, 0.73, 0.76], [0.65, -0.61, 0.16, -0.72], [-0.89, 0.51, -0.46, -0.28]))