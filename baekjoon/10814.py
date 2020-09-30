# 회원수 n 을 입력받음
n = int(input())

# 튜플의 첫번째 요소를 int형으로 변환하는 함수 정의


def change_int(member):
    return (int(member[0]), member[1])


# 회원수 만큼 나이,이름 튜플을 입력받음
member_list = [change_int(input().split()) for i in range(n)]

# 나이순으로 오름차순정렬
member_list.sort(key=lambda member: member[0])

# 정렬된 결과값 출력
[print(f"{member[0]} {member[1]}") for member in member_list]
