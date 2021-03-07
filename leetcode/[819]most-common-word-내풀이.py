import re
from typing import List
from collections import Counter

"""
Runtime: 44 ms
Memory: 14.4 MB

내 생각: 묶여있는 단어 풀어주는 부분의 코드가 조금 복잡했던것같다.
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 소문자로 변환
        paragraph = paragraph.lower()

        # 단어 리스트 생성
        words: List[str] = paragraph.split()

        # "a,a,a,b"와 같이 묶여있는 단어 풀어주기
        for index, word in enumerate(words):
            if word.count(',') > 1:
                words.extend(words.pop(index).split(','))

        # 정규식으로 특수문자 제거
        for index, word in enumerate(words):
            words[index] = re.sub('[^a-z0-9]', '', word)

        # 갯수 카운트
        word_count = Counter(words)

        # ban 단어 제거
        for ban_word in banned:
            try:
                word_count.pop(ban_word)
            except KeyError:
                pass

        return word_count.most_common(1)[0][0]


s = Solution()
paragraph: str = "a, a, a, a, b,b,b,c, c"
banned: List[str] = ["a"]

print(s.mostCommonWord(paragraph, banned))
