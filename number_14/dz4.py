n = 256 ** 56 + 5 ** 1138 - 3405
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

x = convert_to(n, 5)

print(x.count("4"))