import math


def main(b):
    w = {f for f in b if ((f < 62) ^ (f >= -94))}
    z = b.union(w)
    p = {e * o for e in w for o in z if e <= o}
    c = {o ** 2 + math.floor(o / 9) for o in z if ((o <= 54) ^ (o >= -98))}
    u = sum(i % 2 for i in p) - sum(5 * i + math.ceil(k / 9) for i in p
                                    for k in c)
    return u


print(main({1, 3, 43, 76, 13, -81, -15, -76, 59}))
print((-0.96 / 60) ** 3)