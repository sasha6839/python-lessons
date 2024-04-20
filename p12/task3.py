x = (12, 3, 17.256, -5, [1, '2', 'R1'], 'Sanya', 'Dimon', ('1', 1), {}, 'Dima+Tanya')
for g in x:
    if type(g) is list:
        for h in g:
            print(h, ': ', type(h))
    elif type(g) is tuple:
        for h in g:
            print(h, ': ', type(h))
    elif type(g) is dict:
        for h in g:
            print(h, ': ', type(h))
    else:
        print(g, ': ',type(g))