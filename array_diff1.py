def array_diff(a, b):
    for i, l1 in enumerate(a):
        for j, l2 in enumerate(b):
            print(a[i], b[j])
            if a[i] == b[j]:
                del a[i]
    return a

print(array_diff([1, 2, 2], [2]))