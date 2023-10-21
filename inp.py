def inp():
    n = int(input())
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
