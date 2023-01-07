n = 17 ** 189 + 49 ** 342 - 7 ** 104

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

z = convert_to(n, 7)
print(sum(list(z)))
