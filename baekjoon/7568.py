# 전체 사람의 수 n을 입력받음
n = int(input())

# n명의 몸무게,키 값을 튜플로 입력받기
people_list = [tuple(map(int, input().split())) for i in range(n)]

# 덩치 등수가 저장될 리스트
rank_list = []

# people_list에서 덩치 비교해서 rank_list에 값 저장
for people in people_list:
    rank = 1

    for target in people_list:
        if people == target:
            continue
        if (people[0] < target[0] and people[1] < target[1]):
            rank += 1

    rank_list.append(rank)

# 결과값 출력
[print(i, end=" ") for i in rank_list]
