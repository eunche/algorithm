import sys

"""
-리스트로 변환
Runtime: 280 ms
Memory: 19.6 MB

특징 : 리스트의 pop()은 O(n)이므로 이 풀이는 성능이 좋지 않다.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: list = []

        # 알파벳구분, 소문자 변환
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


s = Solution()
print(s.isPalindrome(sys.stdin.readline().strip()))
