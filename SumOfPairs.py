def sum_pairs(ints, s):
    seen = set()
    for number in ints:
        if s - number in seen:
            return [s - number, number]
        seen.add(number)
    return None

print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))