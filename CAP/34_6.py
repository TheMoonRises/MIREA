import math


def main(n):
    a = {abs(v) for v in n if float("-inf") < v < -2}
    psi = {(v % 3) - (v ** 3) for v in n if -27 < v < 45}
    o = a.union(psi)
    b = len({(p, u) for p in psi for u in o}) - sum(q % 2 for q in o)
    return b


print(main({-95, 6, 8, -88, -19, -16, 51, -43, 24, -98}))
print(main({-31, -94, 97, 6, 9, 43, -83, 15, 91, -1}))
print(float("-inf"))
