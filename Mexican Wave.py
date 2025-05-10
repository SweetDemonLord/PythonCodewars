def wave(people):
    #lst = ''.join(list(people))

    # return [''.join(list(people)).replace(list(people)[i],list(people)[i].upper()) for i in range(len(people))]

    return [people[:i] + people[i:].replace(people[i], people[i].upper(), 1)
            for i in range(len(people)) if people[i].isalpha()]
print(wave("insaf"))
print(wave("диметиламиноазобензол"))
print(wave("a            b         "))