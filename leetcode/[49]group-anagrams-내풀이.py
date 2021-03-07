from typing import List

"""
Runtime: 100 ms
Memory: 17.8 MB

책 풀이와 다른점 : 책에서는 defaultdict를 이용해서 15~17번 줄의 작업을 생략할수있었다.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dict에서 key로만 쓰일, 오름차순 정렬된 단어
        tags: list = set(["".join(sorted(s)) for s in strs])

        result_dict = {tag: [] for tag in tags}

        # 애너그램 분류
        for s in strs:
            result_dict["".join(sorted(s))].append(s)

        return result_dict.values()


s = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(*s.groupAnagrams(strs), sep='\n')
