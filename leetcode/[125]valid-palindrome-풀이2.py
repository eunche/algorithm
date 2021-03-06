import sys
import collections

"""
-데크 자료형을 이용한 최적화
Runtime: 52 ms
Memory: 19.4 MB

특징 : 리스트 -> 데크로 바꾸면서, pop이 O(n) -> O(1)로 바뀌어 성능이 많이 향상되었다.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: collections.deque = collections.deque()

        # 알파벳구분, 소문자 변환
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


s = Solution()
print(s.isPalindrome(sys.stdin.readline().strip()))
