def x2(x, left, mid, right):
    if x[2] == "NGINX":
        return left
    elif x[2] == "OPA":
        return mid
    elif x[2] == "D":
        return right


def x1(x, left, right):
    if x[1] == 2009:
        return left
    elif x[1] == 1967:
        return right


def x0(x, left, mid, right):
    if x[0] == 1985:
        return left
    elif x[0] == 1990:
        return mid
    elif x[0] == 1998:
        return right


def x3(x, left, right):
    if x[3] == "EQ":
        return left
    elif x[3] == "VCL":
        return right


def main(x):
    return x2(x, x1(x, x3(x, 0, 1), x3(x, 2, 3)),
              x0(x, 4, 5, x1(x, 6, 7)), x1(x, 8, 9))


print(main([1985, 1967, 'D', 'VCL']))
