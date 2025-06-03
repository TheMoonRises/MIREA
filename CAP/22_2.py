import math
def main(z):
    if z < 66:
        return 88*z
    elif 66 <= z < 124:
        return 15 * z ** 5 - (z ** 3 / 65) - (z ** 7 / 34)
    elif 124 <= z < 191:
        return 30 * z + 1 + (41 * z) ** 4
    elif 191 <= z < 217:
        return (z ** 4 / 91) + 51 * (math.floor(z + 91 * z ** 3 + z ** 2)) ** 7 + (z + z ** 3 / 38) ** 3
    elif z >= 217:
        return 58 * z ** 3

print(main(234))