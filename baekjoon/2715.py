# 입력받을 수의 갯수
n = int(input())

# n개만큼 정수 입력받기
num_list = [int(input()) for i in range(n)]

# 리스트 오름차순으로 정렬
num_list.sort()

# 한줄씩 출력
[print(i) for i in num_list]
