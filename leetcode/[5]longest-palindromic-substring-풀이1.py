"""
-중앙을 중심으로 확장하는 풀이
Runtime: 260 ms
Memory: 14.5 MB

특징: 양끝 비교가 아닌(내풀이), 중앙을 중심으로 확장하며 풀었다.
      홀수일때, 짝수일때를 나눠서 가장긴 팰린드롬을 찾았고, 거기서 또 최대값을 가려냈다
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result


s = Solution()
word: str = "babad"
print(s.longestPalindrome(word))
