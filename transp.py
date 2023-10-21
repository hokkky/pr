def transp(ma):
    g = [[[] for _ in range(len(ma))] for _ in range(len(ma[0]))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j]= ma[j][i]
    return g
