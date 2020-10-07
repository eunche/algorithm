import sys
from collections import deque

# 카드의 갯수 n
n = int(sys.stdin.readline())

# 카드 deque ex) n=4 -> [4,3,2,1]
card_deque = deque([i for i in range(n, 0, -1)])

# 한장의 카드가 남을때까지 반복
while(len(card_deque) > 1):

    # 제일 위에있는 카드 버리기
    card_deque.pop()

    # 제일 위에있는 카드를 제일 아레 있는 카드 밑으로 옮기기
    card_deque.appendleft(card_deque.pop())


# 제일 마지막에 남게되는 카드 출력
print(card_deque[0])
