import sys
from collections import deque

test_case = int(sys.stdin.readline())

# return_item함수와 관련된 전역변수
i = 0

# 중요도 deque의 값으로, map함수의 첫번째 인자로 쓰일 함수


def return_item(x):
    global i
    my_item = (int(x), i)
    i += 1
    return my_item


for _ in range(test_case):
    document_num, target = list(map(int, sys.stdin.readline().split()))
    importance_deque = deque(map(return_item, sys.stdin.readline().split()))
    # print(target, importance_deque)
    i = 0

    count = 1
    while True:
        # print(importance_deque)
        first_element = importance_deque[0]
        max_importance = max(importance_deque, key=lambda x: x[0])
        if max_importance == first_element:
            if first_element[1] == target:
                print(count)
                break
            else:
                count += 1
                importance_deque.popleft()
        else:
            importance_deque.rotate(-1)
