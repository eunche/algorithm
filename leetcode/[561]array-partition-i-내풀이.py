from typing import List

"""
Runtime:  308 ms
Memory:  16.7 MB

내 생각: 2개씩 묶어서 나눌때, min(a,b) 에서 작은것끼리 묶여야 큰값이 sum에 추가 되므로,
         정렬 이후 짝수(index) 값들만 더해 주었다.
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum


nums = [6, 2, 6, 5, 1, 2]
s = Solution()
print(s.arrayPairSum(nums))
