import sys
input = sys.stdin.readline

"""
1^2
1 (N//2+1,N//2+1)

3^2 (i==3)
2 (-1,0)
i-2 3 (0,+1)
i-1 4 (+1,0) 5 (+1,0) / 6 (0,-1) 7 (0,-1) / 8 (-1,0) 9 (-1,0)

5^2 (i==5)
10 (-1,0)
i-2 11 (0,+1) 12 (0,+1) 13 (0,+1)
i-1 14 (+1,0) 15 (+1,0) 16 (+1,0) 17 (+1,0)
"""

def solution(N, k):
    y, x = (N // 2) + 1, (N // 2) + 1
    graph = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
    graph[y][x] = 1
    point = [y, x]
    dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(3, N + 1, 2):
        ny, nx = y + dydx[0][0], x + dydx[0][1]
        graph[ny][nx] = graph[y][x] + 1
        y, x = ny, nx

        for _ in range(i - 2):
            ny, nx = y + dydx[1][0], x + dydx[1][1]
            graph[ny][nx] = graph[y][x] + 1
            y, x = ny, nx

        for l in [2, 3, 0]:
            for _ in range(i - 1):
                ny, nx = y + dydx[l][0], x + dydx[l][1]
                graph[ny][nx] = graph[y][x] + 1
                y, x = ny, nx

    for i in range(1, N + 1):
        for l in range(1, N + 1):
            if graph[i][l] == k:
                point = [i, l]
            print(graph[i][l], end=" ")
        print()
    print(*point, sep=" ")

N = int(input())
k = int(input())
solution(N, k)
