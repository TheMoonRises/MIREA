def main(x: str):
    v = int(x, 16)
    e1 = (v >> 0) & 0x1f
    e2 = (v >> 5) & 0x7f
    e3 = (v >> 12) & 0x7f
    e4 = (v >> 19) & 0x7f
    d = hex(e3 | e4 << 7 | e1 << 14 | e2 << 19)
    return d

print(main('0x350100d'))
print(hex(0b1111))
