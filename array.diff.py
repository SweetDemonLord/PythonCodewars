def array_diff(a, b):
    return list(set(a)^set(b))

l1 = [1, 2, 2, 2, 3]
l2 = [1, 2]
print(array_diff(l1, l2))