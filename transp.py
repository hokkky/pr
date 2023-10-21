def transp(m):
    g = m[::]
    for i in range(len(g)):
        for j in range(len(g[i]) // 2):
            g[i][j], g[j][i] = g[j][i], g[i][j]
    return g