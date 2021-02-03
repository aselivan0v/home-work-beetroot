def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def to_bin(n):
    if n == 0 or n == 1:
        return str(n)
    return to_bin(n // 2) + str(n%2)
#print(to_bin(255))
#print(hex(37))
#print(int('4445', base = 8)

def to_digit(n, base = 10):
    if n <  base:
        return  str(n) if n < 10 else chr(n + 55)
    return to_digit(n//base, base) + str(n%base if n%base < 10 else chr (n%base + 55))

print(to_digit(42, 16))