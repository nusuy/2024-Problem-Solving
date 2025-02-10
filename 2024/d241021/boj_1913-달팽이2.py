import sys
input = sys.stdin.readline

def solution(N, k):
    y, x = (N // 2) + 1, (N // 2) + 1
    graph = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
    graph[y][x] = 1
    point = [y, x]
    dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(3, N + 1, 2):
        for l in range(5):
            if l == 0:
                rng = 1
            elif l == 1:
                rng = i - 2
            else:
                rng = i - 1

            for _ in range(rng):
                ny, nx = y + dydx[l % 4][0], x + dydx[l % 4][1]
                graph[ny][nx] = graph[y][x] + 1
                if graph[ny][nx] == k:
                    point = [ny, nx]
                y, x = ny, nx

    for i in range(1, N + 1):
        print(*graph[i][1:], sep=" ")
    print(*point, sep=" ")

N = int(input())
k = int(input())
solution(N, k)
