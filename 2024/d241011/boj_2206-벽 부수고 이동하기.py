from collections import deque
import sys
input = sys.stdin.readline

def solution(N, M, graph):
    dydx = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    q = deque([(0, 0, 0)])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        y, x, w = q.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][w]

        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and visited[ny][nx][w] == 0:
                    visited[ny][nx][w] = visited[y][x][w] + 1
                    q.append([ny, nx, w])
                elif graph[ny][nx] == 1 and w == 0:
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
                    q.append([ny, nx, w + 1])

    return -1

N, M = map(int, input().split())
graph = [[int(c) for c in input().rstrip()] for _ in range(N)]

print(solution(N, M, graph))
