#!/usr/bin/env python3

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


# recursive version
def fib2(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)



for n in range(1, 10):  # testing
    print(n, "->", fib(n))

print('recursive version:')
for n in range(1, 10):  # testing
    print(n, "->", fib2(n))
