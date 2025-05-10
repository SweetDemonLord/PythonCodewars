import math

def rectangle_rotation(a, b):
    count = 0
    # Bounding box for points to check
    r = int((a + b) / math.sqrt(2)) + 1

    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            # Rotate (x, y) by 45 degrees clockwise
            xr = (x + y) / math.sqrt(2)
            yr = (y - x) / math.sqrt(2)
            if abs(xr) <= a / 2 and abs(yr) <= b / 2:
                count += 1

    return count

def count_integer_points(a, b):
    a_half = a // math.sqrt(2)
    b_half = b // math.sqrt(2)
    max_x = int((a + b) / math.sqrt(2)) + 1
    min_x = -max_x
    count = 0

    for x in range(min_x, max_x + 1):
        lower_y = max(-x - a_half, x - b_half)
        upper_y = min(-x + a_half, x + b_half)
        if lower_y > upper_y:
            continue
        count += upper_y - lower_y + 1

    return count

def rectangle_rotation2(a, b):
    a //= 2**0.5
    b //= 2**0.5
    r = (a + 1) * (b + 1) + a * b

    return r + r % 2 - 1


def rectangle_rotation3(a, b):
    wid_even = 2 * int(a / 2 / (2 ** 0.5)) + 1
    hei_even = 2 * int(b / 2 / (2 ** 0.5)) + 1

    wid_odd = 2 * int(a / 2 / (2 ** 0.5) + 1 / 2)
    hei_odd = 2 * int(b / 2 / (2 ** 0.5) + 1 / 2)

    # wid_even * hei_even is the numbers of points (x,y) that x + y is even
    # others are counted by wid_odd*hei_odd
    return wid_even * hei_even + wid_odd * hei_odd
print((rectangle_rotation(6, 4), 23))
print((rectangle_rotation(30, 2), 65))
print((rectangle_rotation(8, 6), 49))
print((rectangle_rotation(16, 20), 333))



print((count_integer_points(6, 4), 23))
print((count_integer_points(30, 2), 65))
print((count_integer_points(8, 6), 49))
print((count_integer_points(16, 20), 333))


print((rectangle_rotation2(6, 4), 23))
print((rectangle_rotation2(30, 2), 65))
print((rectangle_rotation2(8, 6), 49))
print((rectangle_rotation2(16, 20), 333))