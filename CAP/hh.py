from struct import *

def parse_data(buf, offset, fmt, order='>'):
    d = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[fmt]
    size = calcsize(order + d)
    result = unpack_from(order + d, buf, offset)[0]
    return result, offset + size

def parse_d(buf, offset):
    d1_size, offset = parse_data(buf, offset, 'uint16')
    d1_offset, offset = parse_data(buf, offset, 'uint16')
    d1 = [parse_data(buf, d1_offset + i, 'uint8')[0] for i in range(d1_size)]
    d2_size, offset = parse_data(buf, offset, 'uint32')
    d2_offset, offset = parse_data(buf, offset, 'uint16')
    d2 = [parse_data(buf, d2_offset + i, 'uint8')[0] for i in range(d2_size)]
    d3, offset = parse_data(buf, offset, 'int32')
    return {'D1': d1, 'D2' : d2, 'D3': d3}, offset
def parse_c(buf,offset):
    c1_size, offset = parse_data(buf, offset, 'uint32')
    c1_offset, offset = parse_data(buf, offset, 'uint32')
    c1 = ''
    for _ in range(c1_size):
        val, c1_offset = parse_data(buf, c1_offset, 'char')
        c1 += val.decode('utf-8')
    c2, offset = parse_data(buf, offset, 'int8')
    c3, offset = parse_data(buf, offset, 'int8')
    c4, offset = parse_data(buf, offset, 'int32')
    c5, offset = parse_data(buf, offset, 'int32')
    c6, offset = parse_data(buf, offset, 'uint64')
    c7, offset = parse_data(buf, offset, 'int32')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5, 'C6': c6, 'C7': c7}, offset
def parse_b(buf, offset):
    b1, offset = parse_c(buf, offset)
    b2, offset = parse_data(buf, offset, 'int16')
    return {'B1': b1, 'B2': b2}, offset
def parse_a(buf, offset):
    a1, offset = parse_b(buf, offset)
    a2_size, offset = parse_data(buf, offset, 'uint32')
    a2_offset, offset = parse_data(buf, offset, 'uint32')
    a2 = ''
    for _ in range(a2_size):
        val, a2_offset = parse_data(buf, a2_offset, 'char')
        a2 += val.decode('utf-8')
    a3, offset = parse_data(buf, offset, 'int32')
    a4 = []
    for _ in range(5):
        d, offset = parse_d(buf, offset)
        a4.append(d)
    a5, offset = parse_data(buf, offset, 'int64')
    a6, offset = parse_data(buf, offset, 'int64')
    a7, offset = parse_data(buf, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6, 'A7': a7}, offset
def main(data):
    offset = 4
    return parse_a(data, offset)[0]

print(main((b'DPJ\xfe\x00\x00\x00\x05\x00\x00\x00\x8a\x8e\x1c\x98\x93wV\xb2\xce!g\x91\xd2\x86[\xc8\x9a\x10\xf566|}A\xab\x00\x00\x00\x02\x00\x00\x00\x8f\xb1\xf4\x14\x9d\x00\x03\x00\x91\x00\x00\x00\x03\x00\x94\x0c\xf5\x91\x12\x00\x04\x00\x97\x00\x00\x00\x02\x00\x9b\xfa\xc2\xc0U\x00\x04\x00\x9d\x00\x00\x00\x03\x00\xa1h\x06sw\x00\x04\x00\xa4\x00\x00\x00\x03\x00\xa8V=\xfb\x94\x00\x03\x00\xab\x00\x00\x00\x03\x00\xae\x02X!n\x1d\xe6\xaaG\x1aw\x9c\xc1\xff\xa7\xb6\xab?J8D?h*qvgiaysn\xa5\x96\x92\x18\n\xd5,\xe9\x15}\xb7\x04\x18\xf9\xb6q\x1f\x8d\\%\x11L\x13\xb6\x1bI\x0e\xe3\xa6\xf6)d')))