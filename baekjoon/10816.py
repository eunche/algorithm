from collections import Counter
import sys


# 내가 가진 카드의 갯수 n
n = sys.stdin.readline().strip()

my_card_list = sys.stdin.readline().split()

# case로 나올 카드의 갯수 m
m = sys.stdin.readline().strip()

case_card_list = sys.stdin.readline().split()

my_card_counter = Counter(my_card_list)

count_card_list = []

for card in case_card_list:
    count_card_list.append(str(my_card_counter[card]))

print(" ".join(count_card_list))
