# 입력받을 정수의 갯수 n
n = int(input())

# n개의 정수 입력 받기
num_list = list(map(int, input().split()))

# 출력될 정답의 갯수 m
m = int(input())

# m개로 이루어진 정답 리스트 입력 받기
answer_list = list(map(int, input().split()))

for num in answer_list:
    print(1) if num in num_list else print(0)
