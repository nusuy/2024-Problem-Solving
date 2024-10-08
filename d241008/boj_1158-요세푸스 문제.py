import sys
input = sys.stdin.readline

def solution(N, K):
    q = list()
    for i in range(1, N + 1):
        q.append(i)
    n = K - 1
    for i in range(N):
        if len(q) > n:
            v = q.pop(n)
            n += K - 1
        elif len(q) <= n:
            n = n % len(q)
            v = q.pop(n % len(q))
            n += K - 1

        if i == 0:
            print("<", end="")
        if i < N - 1:
            print(f"{v}, ", end="")
        else:
            print(v, end="")
        if i == N - 1:
            print(">", end="")

N, K = map(int, input().split())
solution(N, K)
