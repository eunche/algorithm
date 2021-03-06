import sys
from typing import List

"""
Runtime: 200 ms
Memory: 18.2 MB

내 생각 : for문을 돌리면 O(n)이 되므로 다른 아이디어를 생각하지 못하고 리스트의 메소드를 이용했다.
***풀이2와 동일풀이
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


s = Solution()

char_list: List[str] = list(sys.stdin.readline().strip())
s.reverseString(char_list)

print(char_list)
