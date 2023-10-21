def mult(m1, m2):
    if len(m1[0]) != len(m2):
        print("Умножение невозможно")
        return 0
    g = [[[] for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            sum = 0
            for k in range(len(m2)):
                sum += m1[i][k] * m2[k][j]
            g[i][j] = sum
    return g