import sys
input = sys.stdin.readline

'''
1. a, e, i, o, u 중 하나 반드시 포함
2. 모음 3개 혹은 자음 3개 연속 X
3. 같은 글자 연속 두번 X, but ee/oo는 허용
'''

def check_v(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

def solution(word):
    v_exist = False
    v_series = [False, False]
    c_series = [False, False]
    prev = ''
    prev_v = False

    for c in word:
        if prev == c:
            if not v_series[1] and (c == 'e' or c == 'o'):
                v_series[1] = True
            else:
                return False

        if check_v(c):
            if not v_exist:
                v_exist = True
            if not prev_v:
                c_series = [False, False]
            if v_series[0]:
                if v_series[1] and c != 'e' and c != 'o':
                    return False
                else:
                    v_series[1] = True
            elif v_series[1]:
                return False
            else:
                v_series[0] = True
            prev_v = True
        else:
            if prev_v:
                v_series = [False, False]
            if c_series[0]:
                if not c_series[1]:
                    c_series[1] = True
                else:
                    return False
            else:
                c_series[0] = True
            prev_v = False
        prev = c

    return v_exist

while True:
    word = input().rstrip()
    if word == "end":
        break

    if solution(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
