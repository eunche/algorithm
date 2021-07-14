from typing import List
from functools import reduce

"""
-시간초과

내 생각: for문 2개를 2중 for문이 아닌 나열해둬서 2n이 될 줄 알았는데, 시간초과가 났다.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        lists = []

        for index, _ in enumerate(nums):
            new_list = nums[:]
            new_list.pop(index)

            lists.append(new_list)

        for l in lists:
            result.append(reduce(lambda x, y: x*y, l))

        return result


nums = [-1, 1, 0, -3, 3]
s = Solution()
print(s.productExceptSelf(nums))
