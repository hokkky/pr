def inp():
    print ("Сперва введите кол-во строк матрицы, затем сами строчки:")
    n = int(input())
    if n<=0:
        print ("Число строк не являлется натуральным числом!")
        exit()
        return 0
    else:
        s = list(map(int, input().split()))
        mat = [s]
        k = len(s)
        for i in range(1, n):
            s = list(map(int, input().split()))
            while len(s) != k:
                print("Введите строку подходящей длины")
                s = list(map(int, input().split()))
            mat.append(s)
        return mat
