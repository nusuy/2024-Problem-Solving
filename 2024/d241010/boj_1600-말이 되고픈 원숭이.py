from collections import deque
import sys
input = sys.stdin.readline

def solution(K, W, H, grid):
    h_dydx = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
              (2, 1), (1, 2), (2, -1), (1, -2)]
    dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        y, x, w = q.popleft()
        if y == H - 1 and x == W - 1:
            return visited[y][x][w] - 1

        if w < K:
            for dy, dx in h_dydx:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != 1 and visited[ny][nx][w + 1] == 0:
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
                    q.append([ny, nx, w + 1])

        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != 1 and visited[ny][nx][w] == 0:
                visited[ny][nx][w] = visited[y][x][w] + 1
                q.append([ny, nx, w])

    return -1

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

print(solution(K, W, H, grid))
