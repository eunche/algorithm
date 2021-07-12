from typing import List

"""
실패

내 생각: 3중 for문까지 코드가 너무 복잡했고, 테스트 케이스를 넣고 틀리고를 반복하며 작성한 코드라 굉장히 난해했다.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        rain_sum: int = 0
        left_right_all: list = []

        # 예외처리
        if len(height) < 3:
            return 0

        # rain_sum 구하기
        i = 1
        while i < len(height)-1:
            if height[i-1] >= height[i] and height[i+1] >= height[i]:
                left_index, right_index = i-1, i+1
                will_remove_height = height[i]

                # 올라가다 내려가는 지점까지 왼쪽으로 이동
                while True:
                    will_remove_height += height[left_index]

                    # break조건 1
                    if left_index - 1 < 0:
                        break
                    # break조건 2
                    if height[left_index-1] < height[left_index]:
                        break

                    left_index -= 1

                # 올라가다 내려가는 지점까지 오른쪽으로 이동
                while True:
                    will_remove_height += height[right_index]

                    # break조건 1
                    if right_index + 1 > len(height) - 1:
                        break
                    # break조건 2
                    if height[right_index+1] < height[right_index]:
                        break

                    right_index += 1

                left_right_all.extend(
                    [(height[left_index], left_index), (height[right_index], right_index)])
                for j in range(left_index, right_index+1):
                    m = min(height[left_index], height[right_index])
                    if height[j] > m:
                        will_remove_height -= height[j] - m

                section_width = right_index - left_index + 1
                section_height = height[left_index] if height[left_index] < height[right_index] else height[right_index]
                section_sum = (section_width * section_height) - \
                    will_remove_height

                # print(section_sum)
                rain_sum += section_sum
                # print(i, left_index, right_index)
                i = right_index
            else:
                i += 1
        print(left_right_all)
        # 양옆이 가두는 경우, 윗줄에 쌓인 빗물 추가
        if len(left_right_all) >= 4:
            for i in range(0, len(left_right_all)-3, 2):
                print(f"i = {left_right_all[i]}")
                for j in range(i+3, len(left_right_all), 2):
                    print(f"j = {left_right_all[j]}")
                    if left_right_all[i] == max(left_right_all[i:j], key=lambda x: x[0]) and left_right_all[j] == max(left_right_all[i+1:j+1], key=lambda x: x[0]):
                        w = left_right_all[j][1] - left_right_all[i][1] - 1
                        h = min(left_right_all[i][0], left_right_all[j][0]) - \
                            max(left_right_all[i+1:j], key=lambda x: x[0])[0]
                        rain_sum += w * h
                        for k in height[left_right_all[i][1]+1:left_right_all[j][1]]:
                            print(k)
                        break
                        # print(
                        # f"i = {left_right_all[i]}    j = {left_right_all[j]}   w*h={w*h}")

        return rain_sum


s = Solution()
height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3,
          2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
print(s.trap(height))
