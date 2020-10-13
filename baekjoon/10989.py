import sys

# 입력받을 수 n
n = int(sys.stdin.readline())

num_dict = {}

for _ in range(n):
    num = int(sys.stdin.readline())

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

sorted_num_items = sorted(num_dict.items(), key=lambda x: x[0])

last_item = sorted_num_items[-1]

for item in sorted_num_items:
    string = f"{item[0]}\n"*item[1]
    string = string[:-1]
    print(string)
