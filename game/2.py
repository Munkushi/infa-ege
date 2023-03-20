# def p(x):
#     for i in range(1, int(x**0.5) + 1):
#         if x % i == 0:
#             return False
#     return True


# first solution

# numbers = None
# maxx = 0
# for i in range(389876, 399999+1):
#     divisors = 0
#     # numbers = None
#     for j in range(1, int(i ** 2) + 1):
#         if i % j == 0:
#             # numbers.add(i)
#             divisors = divisors + 2 if j != i // j else divisors + 1
#             # divisors.add(i // j)
#     if divisors > maxx:
#         maxx = divisors
#         numbers = i
# # print(numbers, maxx)


# second solution

def f(start, end):
    max_div = 0
    numbers = 0
    for n in range(start, end):
        divisors = 0
        for i in range(1, int(n ** 2) + 1):
            if n % i == 0:
                divisors += 2 if i != n // i else 1
        if divisors > max_div:
            max_div = divisors
            numbers = n
    return numbers

print(f(389876, 400_000))



# third solution

# ii = 0

# for i in range(389_876, 399_999+1):
#     divisors = 0
#     for j in range(1, int(i ** 2) + 1):
#         if i % j == 0:
#             divisors += 1
#     if divisors > ii:
#         ii = divisors
#         it = i
# print(ii, it)