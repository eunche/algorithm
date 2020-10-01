# 입력받을 좌표의 수 n
n = int(input())

# n개만큼 좌표를 tuple로 입력받는다
coords_list = [tuple(map(int, input().split())) for i in range(n)]

# 좌표값을 정렬
coords_list = sorted(coords_list)

# 결과값을 출력
[print(f"{coord[0]} {coord[1]}") for coord in coords_list]
