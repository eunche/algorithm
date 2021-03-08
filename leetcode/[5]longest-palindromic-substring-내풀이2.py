"""
Runtime: 8728 ms
Memory: 14.5 MB

내 생각: 풀긴 풀었으나 실행속도가 너무 느렸음.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_p: str = s[0]

        # 주어진 문자열이 한글자일경우 바로 그 값을 리턴
        if len(s) == 1:
            return s

        # 가장 긴 팰린드롬 찾는 작업(첫글자와 맨뒷글자가 같으면 팰린드롬 여부 확인)
        for i in range(len(s)-1):
            if len(longest_p) > len(s) - i:
                break
            for j in range(len(s), i, -1):
                if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(longest_p):
                    longest_p = s[i:j+1]
                    break

        return longest_p


s = Solution()
word: str = "babad"
print(s.longestPalindrome(word))
