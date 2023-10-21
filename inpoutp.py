def inp():
    n = int(input())
    matrix = [list(input().split()) for i in range(n)]
    return matrix

def outp(m):
    print(*m,sep='\n')

outp(inp())
