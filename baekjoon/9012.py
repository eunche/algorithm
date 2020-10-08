import sys
from collections import deque

# 테스트 케이스 수 t
t = int(sys.stdin.readline())

# 케이스 리스트
case_list = [sys.stdin.readline().strip() for _ in range(t)]


# VPS 판별
for case in case_list:

    que = deque()
    is_VPS = False

    for char in case:
        if char == '(':
            que.append(char)
        else:
            if not que:
                is_VPS = False
                break
            else:
                que.pop()
                is_VPS = True

    if que:
        is_VPS = False

    print("YES" if is_VPS else "NO")
