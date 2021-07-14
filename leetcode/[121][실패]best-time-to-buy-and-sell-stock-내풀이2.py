from typing import List

"""
-시간초과

내 생각: 투포인터 풀이로 인해 시간복잡도 O(n)을 만든것같은데, 왜 안되지
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 정답 후보군
        difference = []

        left, right = 0, len(prices) - 1

        while left != len(prices) - 1:
            if prices[left] < prices[right]:
                difference.append(prices[right] - prices[left])

            if left == right:
                left += 1
                right = len(prices) - 1
                continue

            right -= 1

        if not difference:
            return 0

        return max(difference)


prices = [2, 1, 4]
s = Solution()
print(s.maxProfit(prices))
