def a(list):
    ind = []
    for i, vogals in enumerate(list):
        if (vogals == 'a' or 'e' or 'i' or 'o' or 'u'):
            ind.append(i)

    return ind
