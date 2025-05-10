def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
def find_even_index2(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1
print('The first version:')
print(find_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_even_index([1, 2, 1]))
print(find_even_index([7, 0]))
print(find_even_index([0, 7]))
print('The second version:')
print(find_even_index2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_even_index2([1, 2, 1]))
print(find_even_index2([7, 0]))
print(find_even_index2([0, 7]))