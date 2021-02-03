def to_power (x, exp):
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)

def is_palindrome (looking_str):
    if len(looking_str) == 1:
        return True
    if looking_str[0] == looking_str [-1]:
        return is_palindrome(looking_str[1: len(looking_str) -1])
    return False

def sum_of_digits(digit_string):
    if len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])

print(sum_of_digits("33334491"))
print(((2**64)*0.001)/1000)