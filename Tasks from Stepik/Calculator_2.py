""" Converting a number from any number system (up to and including the hexadecimal system) to the decimal system """


def to_dec(num, base):
    dec = list(num)
    power, res, d_16 = 0, 0, {}
    if base > 10:
        val = 10
        for element in range(ord('A'), ord('F') + 1):
            d_16[chr(element)] = val
            val += 1
    while dec:
        next_num = dec.pop()
        next_num = int(next_num) if next_num.isdigit() else d_16[next_num]
        res += next_num * (base ** power)
        power += 1
    return res


n = input('Enter the number: ')
b = int(input('Enter the base of the number: '))
print(f'Decimal Result: {to_dec(n,b)}')