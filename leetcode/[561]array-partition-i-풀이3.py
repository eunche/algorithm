from typing import List

"""
Runtime:  284 ms
Memory:  16.8 MB

특징: 파이써닉한 풀이. 슬라이싱으로 짝수만 뽑아내어 리스트를 만든게 핵심
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


nums = [6, 2, 6, 5, 1, 2]
s = Solution()
print(s.arrayPairSum(nums))
