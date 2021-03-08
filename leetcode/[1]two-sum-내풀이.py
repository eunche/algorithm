from typing import List

"""
Runtime: 48 ms
Memory: 14.5 MB

내 생각: 비효율적인 기본적인 방법으로, 분명 더 좋은 풀이가 있을것같다.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()

nums = [0, 4, 3, 0]
target = 0
print(s.twoSum(nums, target))
