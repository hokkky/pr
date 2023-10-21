from alg import AlgCompl
from outp import outp

def algmat(ma):
    g = ma[::]
    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] = AlgCompl(ma,i,j)
    return g

outp(algmat(input()))