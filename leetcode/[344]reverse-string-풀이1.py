import sys
from typing import List

"""
-투 포인터를 이용한 스왑
Runtime: 196 ms
Memory: 18.3 MB
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = Solution()

char_list: List[str] = list(sys.stdin.readline().strip())
s.reverseString(char_list)

print(char_list)
