import re
from typing import List
from collections import Counter

"""
Runtime: 28 ms
Memory: 14.5 MB
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 정규식 = 단어 문자를 제외하고 모두 공백으로 치환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split() if word not in banned]

        counts = Counter(words)

        return counts.most_common(1)[0][0]


s = Solution()
paragraph: str = "a, a, a, a, b,b,b,c, c"
banned: List[str] = ["a"]

print(s.mostCommonWord(paragraph, banned))
