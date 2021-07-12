from typing import List

"""
-스택 쌓기
Runtime:  108 ms
Memory:  14.9 MB

이해 가지 x
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume


water_lengths = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

s = Solution()
print(s.trap(water_lengths))
