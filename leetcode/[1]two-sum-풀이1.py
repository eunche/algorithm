from typing import List

"""
Runtime: 40 ms
Memory: 14.5 MB

특징: 시간복잡도는 같은 O(n^2) 이지만, in연산이 내부적으로 빠르게 구현되어 있기 때문에 2중for문보다 실행속도가 빠르다.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]


s = Solution()

nums = [0, 4, 3, 0]
target = 0
print(s.twoSum(nums, target))
