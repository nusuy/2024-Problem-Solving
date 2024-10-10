import sys
input = sys.stdin.readline

"""
(0,0) - (N-1, M-1)

d -> n0 e1 s2 w3
 0
3  1
  2
0: 빈 칸 / 1: 벽

1. 현재 칸 청소 X -> 청소
2. 현재 칸 주변 4칸 검사 (청소 안 된 칸 존재 여부)
    a. 미존재 - 응시 방향에서 뒷 칸 검사 (이동 가능: 후진 -> 1번/이동 불가능: 작동 중단)
    b. 존재 - 반시계 방향 90도 회전 -> 응시 방향 기준 앞 칸이 청소 안 된 빈칸이라면 한 칸 전진 -> 1번
"""

def solution(N, M, r, c, d, grid):
    answer = 0
    dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    y, x, dd = r, c, d
    while True:
        if grid[y][x] == 0:
            grid[y][x] = 2
            answer += 1

        is_clean = True
        for dy, dx in dydx:
            ny, nx = y + dy, x + dx
            if 0 < ny < N - 1 and 0 < nx < M - 1 and grid[ny][nx] == 0:
                is_clean = False
                break

        if is_clean:
            nd = (dd + 2) % 4
            ny, nx = y + dydx[nd][0], x + dydx[nd][1]
            if 0 < ny < N - 1 and 0 < nx < M - 1 and grid[ny][nx] != 1:
                y, x = ny, nx
            else:
                break
        else:
            nd = (dd + 3) % 4
            ny, nx = y + dydx[nd][0], x + dydx[nd][1]
            dd = nd
            if 0 < ny < N - 1 and 0 < nx < M - 1 and grid[ny][nx] == 0:
                y, x = ny, nx

    return answer

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

print(solution(N, M, r, c, d, grid))
