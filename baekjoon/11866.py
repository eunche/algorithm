import sys

n, k = map(int, sys.stdin.readline().split())

num_list = [[str(i+1), False] for i in range(n)]

result = []

current = 0
try_count = 0
is_target = 0
while try_count < n:
    while True:
        current = 1 if (current+1) > n else (current+1)
        is_target = (
            is_target+1) if (num_list[current-1][1] == False) else is_target
        if is_target == k:
            result.append(num_list[current-1][0])
            num_list[current-1][1] = True
            is_target = 0
            break
    try_count += 1

print("<"+", ".join(result)+">")
