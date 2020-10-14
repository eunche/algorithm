import sys

# k = 이미 갖고있는 랜선의 수 / n = 필요한 랜선의 수
k, n = map(int, sys.stdin.readline().split())

# 이미 존재하는 랜선 리스트
exists = [int(sys.stdin.readline().strip()) for _ in range(k)]

max_len = round(sum(exists)/n)


"""
시간초과 나온 알고리즘
"""


# for l in range(max_len, 0, -1):
#     lan_count = 0

#     for lan in exists:
#         lan_count += lan//l

#     if lan_count == n:
#         print(l)
#         break


"""
이진탐색으로 시간줄인 알고리즘
"""


def binary_search():
    start = 1
    end = max_len
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        lan_count = 0
        for lan in exists:
            lan_count += lan//mid

        if lan_count < n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)


binary_search()
