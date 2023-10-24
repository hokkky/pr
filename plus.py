def plus(m1, m2):
    if len(m1[0]) != len(m2[0]) or len(m1) != len(m2):
        print("Сложение невозможно")
        return 0
    g = [[[] for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = m1[i][j] + m2[i][j]
    return g


