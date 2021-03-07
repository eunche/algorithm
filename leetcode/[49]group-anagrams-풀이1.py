from typing import List
from collections import defaultdict

"""
Runtime: 92 ms
Memory: 17.2 MB
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


s = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(*s.groupAnagrams(strs), sep='\n')
