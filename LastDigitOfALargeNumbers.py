def last_digit(n1, n2):
    pow_dict = dict(zip(range(1, 10), [1, 4, 4, 2, 1, 1, 4, 4, 2]))
    for key, value in pow_dict.items():
        if n1 % 10 == key:
            return 1 if n2 == 0 else (n1 ** (n2 % value if n2 % value != 0 else value)) % 10
    return 1 if n2 == 0 else 0
def last_digit2(n1, n2):
    return pow(n1, n2, 10)
def better_last_digit(n1, n2):
    if n2 == 0:
        return 1
    last_n1 = n1 % 10
    if last_n1 == 0:
        return 0
    cycles = {
        0: 1,
        1: 1,
        2: 4,
        3: 4,
        4: 2,
        5: 1,
        6: 1,
        7: 4,
        8: 4,
        9: 2
    }
    cycle = cycles[last_n1]
    exponent = n2 % cycle
    if exponent == 0:
        exponent = cycle
    return (last_n1 ** exponent) % 10
print("Last digit 1")
print(last_digit(4, 1)) # returns 4
print(last_digit(4, 2)) # returns 6
print(last_digit(9, 7)) # returns 9
print(last_digit(10, 10 ** 10)) # returns 0
print(last_digit(2**200, 2**300)) # returns 6
print(last_digit(0, 0)) # returns 1
print(last_digit(0, 1)) # returns 0
print(last_digit(5, 0)) # returns 1
print("Last digit 2")
print(last_digit2(4, 1)) # returns 4
print(last_digit2(4, 2)) # returns 6
print(last_digit2(9, 7)) # returns 9
print(last_digit2(10, 10 ** 10)) # returns 0
print(last_digit2(2**200, 2**300)) # returns 6
print(last_digit2(0, 0)) # returns 1
print(last_digit2(0, 1)) # returns 0
print(last_digit2(5, 0)) # returns 1
print("Better Last digit")
print(better_last_digit(4, 1)) # returns 4
print(better_last_digit(4, 2)) # returns 6
print(better_last_digit(9, 7)) # returns 9
print(better_last_digit(10, 10 ** 10)) # returns 0
print(better_last_digit(2**200, 2**300)) # returns 6
print(better_last_digit(0, 0)) # returns 1
print(better_last_digit(0, 1)) # returns 0
print(better_last_digit(5, 0)) # returns 1