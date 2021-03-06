import re
from typing import List

"""
Runtime: 36  ms
Memory: 14.5 MB
특징: 2개의 키를 람다표현식으로 정렬한것이 핵심
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


s = Solution()

input
print(s.reorderLogFiles(["a1 9 2 3 1", "g1 act car",
                         "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]))
