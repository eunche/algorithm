from typing import List

"""
-투 포인터 풀이
Runtime:  64 ms
Memory:  14.8 MB

특징 : 가장 높은곳은 부피에 영향을 주지 않고, 투포인터가 양끝에서
       이동해서 가장 높은곳으로 가며 부피를 더해가는 방법
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


water_lengths = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

s = Solution()
print(s.trap(water_lengths))
