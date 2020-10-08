import sys
from collections import deque

# 정수의 갯수 k
k = int(sys.stdin.readline().strip())

# que 초기화
que = deque()

for _ in range(k):
    num = int(sys.stdin.readline().strip())

    if num == 0 and que:
        que.pop()
    else:
        que.append(num)

print(sum(que))
