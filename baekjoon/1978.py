# 입력받을 자연수의 갯수 n
n = int(input())

# n개의 자연수 리스트
num_list = list(map(int, input().split()))

# 소수의 갯수 카운터
prime_number_count = 0


# 자연수의 소수를 구하는 알고리즘
for num in num_list:
    # num = 1 이면 소수가 아니므로 continue
    if (num == 1):
        continue

    is_prime_num = True
    for i in range(num, 0, -1):
        # 1 or 자기자신이면 continue
        if i == num or i == 1:
            continue
        if ((num % i) == 0):
            is_prime_num = False
            break

    # 1 or 자기자신 이외에 나누어떨어지는 수가 없으면 소수 갯수에 카운트
    if is_prime_num:
        prime_number_count += 1

# 최종 소수 갯수 출력
print(prime_number_count)
