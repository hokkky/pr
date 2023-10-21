def inp():
    n = int(input())
    matrix = [list(input().split()) for i in range(n)]
    return matrix

def outp(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print('\n')

outp(inp())
