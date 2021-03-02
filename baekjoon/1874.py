import sys
from collections import deque

# 입력받을 수 n
n = int(sys.stdin.readline())

# 1~n까지 오름차순 돼있는 덱 정의
init_deq = deque([i for i in range(1, n+1)])

# 덱 선언
deq = deque()

# +,-를 담을 덱
result_deq = deque()

# 사용자가 입력한 값을 모아놓는 덱
input_deq = deque(int(sys.stdin.readline()) for i in range(n))

for num in input_deq:
    # 덱이 비어있으면
    if not deq:
        while True:
            poped_num = init_deq.popleft()
            if poped_num == num:
                result_deq.append("+")
                result_deq.append("-")
                break
            deq.append(poped_num)
            result_deq.append("+")
    # 덱이 안비어있으면
    else:
        if deq[-1] == num:
            deq.pop()
            result_deq.append("-")
        elif num in init_deq:
            for i in range(init_deq.index(num)+1):
                deq.append(init_deq.popleft())
                result_deq.append("+")
            deq.pop()
            result_deq.append("-")
        else:
            result_deq.clear()
            result_deq.append("NO")
            break


for i in result_deq:
    print(i)
