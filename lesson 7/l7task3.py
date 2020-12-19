#A simple calculator.
#Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
#the call make_operation(‘+’, 7, 7, 2) should return 16
#the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#the call make_operation(‘*’, 7, 6) should return 42

def make_operation(x, *args):
    result = 0
    if x == '+':
        for q in args:
            result += q
        return print(result)
    elif x == '-':
        t = 1
        r = args[0]
        while t < len(args):
            r = r - args[t]
            t += 1
            return print(r)

make_operation('+', 7, 7, 2)
make_operation('-', 6, 5, -10, -10)