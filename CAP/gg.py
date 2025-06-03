from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)

def parse(buf, offs, ty, order='>'):
    pattern = FMT[ty]
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size
def parse_d(buf, offs):
    d1size, offs = parse(buf, offs, 'uint16')
    d1offs, offs = parse(buf, offs, 'uint16')
    d1 = []
    for _ in range(d1size):
        val, d1offs = parse(buf, d1offs, 'uint8')
        d1.append(val)
    d2size, offs = parse(buf, offs, 'uint32')
    d2offs, offs = parse(buf, offs, 'uint16')
    d2 = []
    for _ in range(d1size):
        val, d2offs = parse(buf, d2offs, 'uint8')
        d2.append(val)
    d3, offs = parse(buf, offs, 'int32')
    return dict(D1=d1, D2=d2, D3=d3), offs
def parse_c(buf,offs):
    c1size, offs = parse(buf, offs, 'uint32')
    c1offs, offs = parse(buf, offs, 'uint32')
    c1 = []
    for _ in range(c1size):
        val, c1offs = parse(buf, offs, 'char')
        c1.append(val)
    c2, offs = parse(buf, offs, 'int8')
    c3, offs = parse(buf, offs, 'int8')
    c4, offs = parse(buf, offs, 'int32')
    c5, offs = parse(buf, offs, 'int32')
    c6, offs = parse(buf, offs, 'int64')
    c7, offs = parse(buf, offs, 'int32')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7), offs
def parse_b(buf, offs):
    b1, offs = parse_c(buf, offs)
    b2, offs = parse(buf, offs, 'int16')
    return dict(B1=b1, B2=b2), offs
def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2size, offs = parse(buf, offs, 'uint32')
    a2offs, offs = parse(buf, offs, 'uint32')
    a2 = []
    for _ in range(a2size):
        val, a2offs = parse(buf, a2offs, 'char')
        a2.append(val)
    a3, offs = parse(buf, offs, 'int32')
    a4 = []
    for _ in range(5):
        d, offs = parse_d(buf, offs)
        a4.append(d)
    a5, offs = parse(buf, offs, 'int64')
    a6, offs = parse(buf, offs, 'int64')
    a7, offs = parse(buf, offs, 'float')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7), offs

def main(stream):
    res, _ = parse_a(stream, 5)
    return res