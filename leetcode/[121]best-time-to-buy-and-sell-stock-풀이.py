from typing import List
import sys


"""
Runtime:  1092 ms
Memory:  25 MB

특징: x,y그래프를 그려서 시각적으로 보면 풀이법이 생각 날 수 있다.(다른 알고리즘 문제에도 적용하자)
내 생각: 브루트포스와 같은 알고리즘으로만 접근 하려고 했다. 하나의 길 말고 다른 여러 방법들(알고리즘 공부하면서 익혀서)을 적용시키는 연습이 필요 할 것 같다.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))
