from multP import mult_p
def extent(m, x):
    if x<=0 or len(m)!=len(m[0]):
        print ("Возведение в степень невозможно!")
        return 0
    else:
        if x==1: return mult_p(m, 1)
        else:
            m2 = m
            for _ in range (x-1):
                g = [[0]*len(m) for j in range(len(m))]
                for i in range(len(m)):
                    for j in range(len(m)):
                        for k in range(len(m)):
                            g[i][j] += m[i][k] * m2[k][j]
                m = g
            return g
