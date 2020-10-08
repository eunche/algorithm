import sys
from collections import deque

# 명령어의 수 n
n = int(sys.stdin.readline())

# deque 초기화
que = deque()

# n개의 명령어를 실행
for _ in range(n):
    command = sys.stdin.readline().replace("\n", "")
    if command.split()[0] == 'push':
        que.append(command.split()[1])
    elif command == 'pop':
        print(que.popleft() if que else -1)
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        print(1 if not que else 0)
    elif command == 'front':
        print(que[0] if que else -1)
    elif command == 'back':
        print(que[-1] if que else -1)
