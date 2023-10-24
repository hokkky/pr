def mult_p(m1, p):
    
    g = [[[] for j in range(len(m1[0]))] for i in range(len(m1))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = m1[i][j]*p
    return g
