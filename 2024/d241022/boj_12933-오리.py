import sys
input = sys.stdin.readline

"""
quqacukqauackck
1qu / 2q / ac / u / kq / a / uack / ck
1qu/2q/ac/u/k/1q/a/uack/ck
"""

def solution(S):
    answer = 0
    duck = 'quack'
    arr = [0 for _ in range(len(S) // 5)]

    def check_arr(idx):
        for i in range(len(arr)):
            if arr[i] % 5 == idx:
                arr[i] += 1
                return True
        return False

    for c in S:
        for i, v in enumerate(duck):
            if c == v:
                if not check_arr(i):
                    return -1
                break

    for a in arr:
        if a != 0:
            if a % 5 == 0:
                answer += 1
            else:
                return -1
    if answer == 0:
        return -1
    else:
        return answer

S = input()
print(solution(S))
