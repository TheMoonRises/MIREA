def x0(x, left, right):
    if x[0] == 2015:
        return left
    elif x[0] == 1958:
        return right


def x1(x, left, mid, right):
    if x[1] == "MIRAH":
        return left
    elif x[1] == "MQL5":
        return mid
    elif x[1] == "E":
        return right


def x2(x, left, right):
    if x[2] == "SCALA":
        return left
    elif x[2] == "MTML":
        return right


def x3(x, left, mid, right):
    if x[3] == "VUE":
        return left
    elif x[3] == "HYPHY":
        return mid
    elif x[3] == "MQL5":
        return right


def x4(x, left, right):
    if x[4] == 2018:
        return left
    elif x[4] == 2008:
        return right


def main(x):
    return x0(x, x3(x, x2(x, x1(x, 0, 1, 2), x1(x, 3, 4, 5)),
                    x2(x, 6, x4(x, 7, 8)), x2(x, 9, 10)), 11)

print(main([2015, 'MQL5', 'SCALA', 'VUE', 2018]))
print(main([1958, 'MIRAH', 'SCALA', 'HYPHY', 2008]))
print(main([2015, 'MIRAH', 'MTML', 'VUE', 2018]))
print(main([2015, 'E', 'MTML', 'HYPHY', 2008]))
print(main([2015, 'MQL5', 'MTML', 'MQL5', 2018]))
