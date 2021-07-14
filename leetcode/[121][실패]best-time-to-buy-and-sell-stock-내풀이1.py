from typing import List

"""
-시간초과

내 생각: 시간복잡도 O(n^2) 이라서 실패한것같다.
특징: 2중for문 사용
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 가격이 점점 낮아지는 경우, 이익을 볼 수 없으므로 0을 return
        if prices == sorted(prices, reverse=True):
            return 0

        difference = []

        for i in range(0, len(prices)-1, 1):
            compare_list = [x - prices[i]
                            for x in prices[i+1:]]
            if not compare_list:
                continue
            else:
                difference.append(max(compare_list))

        return max(difference)


prices = [7, 6, 4, 3, 1]
s = Solution()
print(s.maxProfit(prices))
