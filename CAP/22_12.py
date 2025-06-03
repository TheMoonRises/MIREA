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


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size

def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int8')
    e2, offs = parse(buf, offs, 'int64')
    e3, offs = parse(buf, offs, 'int32')
    e4, offs = parse(buf, offs, 'int32')
    e5size, offs = parse(buf, offs, 'uint32')
    e5offs, offs = parse(buf, offs, 'uint16')
    e5 = []
    for _ in range(e5size):
        val, e5offs = parse(buf, e5offs, 'float')
        e5.append(val)
    e6, offs = parse(buf, offs, 'int32')
    e7size, offs = parse(buf, offs, 'uint32')
    e7offs, offs = parse(buf, offs, 'uint16')
    e7 = []
    for _ in range(e7size):
        val, e7offs = parse(buf, e7offs, 'double')
        e7.append(val)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7), offs

def parse_d(buf,offs):
    d1, offs = parse(buf, offs, 'uint64')
    d2, offs = parse(buf, offs, 'int8')
    return dict(D1=d1, D2=d2), offs

def parse_c(buf, offs):
    c1 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint32')
        c1.append(val)
    c2 = []
    for _ in range(4):
        c, offs = parse_d(buf, offs)
        c2.append(c)
    c3size, offs = parse(buf, offs, 'uint16')
    c3offs, offs = parse(buf, offs, 'uint16')
    c3 = []
    for _ in range(c3size):
        val, c3offs = parse(buf, c3offs, 'uint16')
        c3.append(val)
    c4, offs = parse(buf, offs, 'uint32')
    c5, offs = parse(buf, offs, 'int64')
    c6, offs = parse_e(buf, offs)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6), offs
def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'int8')
    b2, offs = parse(buf, offs, 'uint64')
    b3, offs = parse(buf, offs, 'uint32')
    b4, offs = parse(buf, offs, 'int8')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4), offs
def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse_c(buf, offs)
    a3, offs = parse(buf, offs, 'double')
    a4, offs = parse(buf, offs, 'uint16')
    a5, offs = parse(buf, offs, 'int32')
    a6, offs = parse(buf, offs, 'float')
    a7, offs = parse(buf, offs, 'double')
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7), offs

def main(stream):
    res, _ = parse_a(stream, 5)
    return res

print(main(b'KCOW\xb0\x90\xd1k\x14\xda\xc0\xaaf\xf7\x13\x9b\tR\xdal\xb4o-\xe9'
 b'\x18\xf2\x02\xa7\x07\x83v/\x05\xf49YMQ\xbdF\xb0\xf1\x8dI}D\xa5e2\xa6;\xf2'
 b'\xc9:;@S^1\xbd\x9d\xbc\xffEpK+\x03\x00\x8e\x00P\xa9"\x1e\xd0(\x0e\x93\xe0'
 b'\x98\x0c\xcb\xae\x90\xd3\xf9g!?\x00\xe8\xf7\xe1\x9a\x08\x1by\xbdS'
 b'\x02\x00\x00\x00\x94\x00\x9f\xd3*7\x02\x00\x00\x00\x9c\x00\xbaH\xb9\xd8'
 b'-\xfe\xe3\xbf\x9dV\x0erVb\xac\xf6s\xbf\xc0\x08\x11m`L\x93\xbfZHF3\xe5J'
 b'\x95\x90\x9d<l\xb8\t?h\xee\xe8\x81\xd7\xa1\xc9?\xe8J\xaa\xac|\xe1\xc8?'))