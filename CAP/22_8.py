def main(decimal_string):
    data = int(decimal_string)
    z1 = data & 0x3F
    z2 = (data >> 6) & 0x3FF
    z3 = (data >> 16) & 0x3
    z4 = (data >> 18) & 0x3
    z5 = (data >> 20) & 0x7F
    z6 = (data >> 27) & 0x3
    result = {
        'Z1': str(z1),
        'Z2': str(z2),
        'Z3': str(z3),
        'Z4': str(z4),
        'Z5': str(z5),
        'Z6': str(z6)
    }
    return result

# Пример использования функции
decimal_string = "523472915"
decoded_data = main(decimal_string)
print(decoded_data)