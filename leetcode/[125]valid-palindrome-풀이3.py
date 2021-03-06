import sys
import re

"""
-슬라이싱 사용
Runtime: 32 ms
Memory: 15.7 MB

특징 : 문자열 슬라이싱은 내부적으로 C로 빠르게 구현되어 있어 성능이 좋다.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]    # 슬라이싱


s = Solution()
print(s.isPalindrome(sys.stdin.readline().strip()))
