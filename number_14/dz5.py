n = 14 ** 78 + 7 * (61 ** 26) - 13 * (12**33) + 2 * (19 ** 15) + 13414
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

z = convert_to(n, 11)

print(z)