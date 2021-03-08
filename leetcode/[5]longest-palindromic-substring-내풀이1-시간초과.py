class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_p: str = ""

        # 주어진 문자열이 한글자일경우 바로 그 값을 리턴
        if len(s) == 1:
            return s

        # 가장 긴 팰린드롬 찾는 작업
        for i in range(len(s)-1):
            for j in range(i, len(s)):
                picked_word: str = s[i:j+1]
                if picked_word == picked_word[::-1] and len(picked_word) > len(longest_p):
                    longest_p = picked_word

        return longest_p


s = Solution()
word: str = "babad"
print(s.longestPalindrome(word))
