import sys
from collections import Counter

# 입력받을 수의 갯수 n
n = int(sys.stdin.readline())

# n개의 수 리스트
num_list = [int(sys.stdin.readline()) for i in range(n)]

# 리스트 요소들의 총합
list_sum = sum(num_list)

# 리스트의 길이
list_len = len(num_list)

# 오름차순으로 정렬한 리스트
sorted_list = sorted(num_list)

# 최빈값을 구하는 함수 정의


def get_mode(sorted_list):
    modes = Counter(sorted_list).most_common(2)
    if n == 1:
        print(sorted_list[0])
    else:
        print(modes[1][0] if modes[0][1] == modes[1][1] else modes[0][0])


"""
최종결과 출력
"""
# 산술 평균(소수점 이하 첫째 자리에서 반올림한 값)
print(round(list_sum/list_len))

# 중앙값
print(sorted_list[list_len//2])


# 최빈값(여러 개 있을 때에는 최빈값 중 두 번째로 작은 값)
get_mode(sorted_list)

# 범위
print(max(num_list) - min(num_list))
