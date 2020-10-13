from collections import deque
import sys

# 명령의 수 n
n = int(sys.stdin.readline())

# 덱 선언
deq = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deq.append(command[1])
    elif command[0] == 'push_back':
        deq.appendleft(command[1])
    elif command[0] == 'pop_front':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif command[0] == 'back':
        if deq:
            print(deq[0])
        else:
            print(-1)
