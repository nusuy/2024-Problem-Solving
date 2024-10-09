import sys
input = sys.stdin.readline

"""
스위치 번호 a, 자신 번호 b
남: a%b == 0인 스위치 상태 변경
여: b 중심 좌우 대칭으로 최대 스위치 포함 구간 상태 변경
"""

def solution(N, switch, M, student):
    for g, s in student:
        if g == 1:
            for i in range(1, (N // s) + 1):
                switch[i * s - 1] = (switch[i * s - 1] + 1) % 2
        elif g == 2:
            switch[s - 1] = (switch[s - 1] + 1) % 2
            left, right = s - 1, s + 1
            while 0 < left and right <= N:
                if switch[left - 1] != switch[right - 1]:
                    break
                v = (switch[left - 1] + 1) % 2
                switch[left - 1], switch[right - 1] = v, v
                left -= 1
                right += 1

    for i in range(1, N // 20 + 2):
        n = i - 1
        if n * 20 + 20 >= N:
            print(*(switch[n * 20:]))
        else:
            print(*(switch[n * 20:n * 20 + 20]))

N = int(input())
switch = list(map(int, input().split()))
M = int(input())
student = []
for _ in range(M):
    student.append(list(map(int, input().split())))

solution(N, switch, M, student)
