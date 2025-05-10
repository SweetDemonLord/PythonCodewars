def high(x):
    scoring_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
                    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
                    'w': 23, 'x': 24, 'y': 25, 'z': 26}

    list_of_scores = []
    for word in x.split():
        score = 0
        for letter in word:
            score += scoring_dict[letter]
        list_of_scores.append(score)

    return x.split()[list_of_scores.index(max(list_of_scores))]
def high2(x):
    return max(x.split(), key=lambda w: sum(ord(c) - 96 for c in w))
print(high('man i need a taxi up to ubud')) # taxi
print(high('dad add')) # taxi

print(high2('man i need a taxi up to ubud')) # taxi
print(high2('dad add')) # taxi