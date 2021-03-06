import sys

"""
Runtime: 40 ms
Memory: 14.7 MB

내 생각 : 실행속도는 빨랐으나, special_chars를 내가 임의로 선언해서 제거할 문자들을 넣어준게 어색한 방법인것같다.
실수로 특정 특수문자를 빼먹을수도 있을것같다.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_chars: str = "`~!@#$%^&*()_+|][}{';\":/?.>,<-="

        # 입력받은 문장에서 특수문자,공백 제거
        for c in special_chars:
            s = s.replace(c, "")
        s = s.replace(" ", "")

        # 문장을 전부 소문자로 변환
        s = s.lower()

        # 팰린드롬 판별
        if s == s[::-1]:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(sys.stdin.readline().strip()))
