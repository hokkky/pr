from inp import inp
from outp import outp
from transp import transp 
def DeleteRowAndColumn(ma,m, n):
    k = [[ma[a-1][b-1] for b in range(1,len(ma[a-1])+1) if b !=n] for a in range(1,len(ma)+1) if a !=m]
    return k

def determinant(ma):
    if len(ma)!=len(ma[0]):
        print ("Матрица не является квадратной. Определитель вычислить невозможно!")
        return '!'
    else:
        if len(ma) == 1 : return ma[0][0]
        else:
            k = 0
            for i in range(1,len(ma)+1):
                k+=ma[i-1][0]*AlgCompl(ma,i,1)
            return k

def AlgCompl(ma,m,n):
    return ((-1)**(m+n))*determinant(DeleteRowAndColumn(ma,m,n))

def algmat(ma):
    if len(ma)!=len(ma[0]):
        print("Матрица не является квадратной. Алгебраические дополнения вычислить невозможно!")
        return 0
    else:
        g = [[[] for i in range(len(ma))] for i in range(len(ma))]
        for i in range(len(g)):
            for j in range(len(g[i])):
                g[i][j] = AlgCompl(ma,i + 1,j + 1)
        return g

def inverseMatrix(ma):
    if len(ma)!=len(ma[0]):
        print("Матрица не является квадратной - найти обратную невозможно!")
        return '?'
    else:
        detMa = determinant(ma)
        if detMa == 0:
            print("Матрица вырожденная - найти обратную невозможно!")
            return '?'
        else:
            AlgMatrix=algmat(ma)
            AlgMatrix=transp(AlgMatrix)
            return [[round((1/detMa),2)*b for b in a] for a in AlgMatrix]

