def snail3(snail_map):
    if not snail_map:
        return []

    result = []
    top, bottom = 0, len(snail_map) - 1
    left, right = 0, len(snail_map[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right (top row)
        for i in range(left, right + 1):
            result.append(snail_map[top][i])
        top += 1
        print('Top', top, result)
        # Traverse from top to bottom (right column)
        for i in range(top, bottom + 1):
            result.append(snail_map[i][right])
        right -= 1
        print('Right', right, result)
        if top <= bottom:  # Check if there's a row left
            # Traverse from right to left (bottom row)
            for i in range(right, left - 1, -1):
                result.append(snail_map[bottom][i])
            bottom -= 1
        print('Bottom', bottom, result)
        if left <= right:  # Check if there's a column left
            # Traverse from bottom to top (left column)
            for i in range(bottom, top - 1, -1):
                result.append(snail_map[i][left])
            left += 1
        print('Left', left, result)
    return result


import numpy as np


def snail2(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        print(out)
        array = list(zip(*array))[::-1]  # Rotate
    return out


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
print(snail(array))  #=> [1,2,3,4,5,6,7,8,9]
