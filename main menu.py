from multP import mult_p
from minus import minus
from plus import plus
from inp import inp
from outp import outp
from mult import mult
from extent import extent
from transp import transp
from rank import rank
from alg import *


def main():
    print("Введите матрицу")
    m1 = inp()
    print("«Вычислить определитель» - введите 'det'")
    print("«Транспонировать» - введите 'TR'")
    print("«Возвести в степень n» - введите '**'")
    print("«Найти обратную матрицу» - введите '-1'")
    print("«Умножить матрицу на число» - введите '*p'")
    print("«Сложить с другой матрицей» - введите '+'")
    print("«Вычесть другую матрицу» - введите '-'")
    print("«Умножить на другую матрицу» - введите '*'")
    print("«Вывести матрицу, состоящую из алгебраических дополнений соответствующих элементов» - введите 'alg'")
    print("«Вычислить ранг матрицы» - введите 'rang'")

    oper = input()
    if (oper == 'TR'): outp(transp(m1))
    elif (oper == 'det'):
        if determinant(m1) == '!': return 0
        print(determinant(m1))
    elif (oper == 'rang'): print(rank(m1))
    elif (oper == 'alg'): outp(algmat(m1))
    elif (oper == '**'):
        if extent(m1) == 0: return 0
        outp(extent(m1))
    elif (oper == '-1'):
        if inverseMatrix(m1) == '?': return 0
        outp(inverseMatrix(m1))
    elif (oper == '*p'):
        print("Введи число, на которое необходимо умножить матрицу")
        p = float(input())
        outp(mult_p(m1, p))
        
    elif (oper == '+'):
        print("Введите ещё одну матрицу")
        m2 = inp()
        if plus(m1,m2)==0: return 0
        outp(plus(m1, m2))
        
    elif (oper == '-'):
        print("Введите ещё одну матрицу")
        m2 = inp()
        if minus(m1,m2)==0: return 0
        outp(minus(m1, m2))
        
    elif (oper == '*'):
        print("Введите ещё одну матрицу")
        m2 = inp()
        if mult(m1,m2)==0: return 0
        outp(mult(m1, m2))

main()
    
        
    
