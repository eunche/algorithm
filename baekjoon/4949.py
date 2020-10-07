import sys
from collections import deque


# "."이 입력될때까지 문장을 sentence_deque에 추가
while(True):

    # 문장을 입력받음
    sentence = sys.stdin.readline().replace("\n", "")

    # 문장이 "."이면 종료조건이므로 while문을 빠져나옴
    if sentence == ".":
        break

    """ 균형 검사 """
    # 괄호 deque
    match_deque = deque()

    # 균형이 맞는지 확인하는 변수
    is_balanced = True

    for char in sentence:

        # 시작 괄호라면 deque에 append
        if (char == '[') or (char == '('):
            match_deque.append(char)

        # 닫는 괄호 ']' 라면 ...
        elif char == ']':
            # 비어있거나 짝이 맞지 않는다면 False
            if (not match_deque or match_deque[-1] == '('):
                is_balanced = False
                break
            # stack의 가장위에 '['가 있다면  stack에서 제거
            elif match_deque[-1] == '[':
                match_deque.pop()

        # 닫는 괄호 ')' 라면 stack에서 제거, 아니면 'no'출력 후 for문 break
        elif char == ')':
            # 비어있거나 짝이 맞지 않는다면 False
            if not match_deque or match_deque[-1] == '[':
                is_balanced = False
                break
            elif match_deque[-1] == '(':
                match_deque.pop()

    # 균형 맞는 문장이라면 'yes'출력
    if (is_balanced and not match_deque):
        print('yes')
    else:
        print('no')
