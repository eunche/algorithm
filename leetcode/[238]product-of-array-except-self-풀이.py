from typing import List

"""
시간복잡도 : O(n)

내 생각: [1,2,3,4]를 예시로,
         left =   [1, 1, 2, 6]
         right =  [24, 12, 4, 1]
         result = [24, 12, 8, 6]
         이 되는데, result[i] = left[i]*right[i] 라는걸 보면 알겠고, 왜 인지는 알겠지만
         이 아이디어를 안보고는 절대 떠올릴 수 없을것 같다.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = []

        p = 1
        for i in range(0, len(nums), 1):
            left.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(p)
            p *= nums[i]

        right.reverse()

        result = [left[i]*right[i] for i in range(len(nums))]

        return result


nums = [-1, 1, 0, -3, 3]
s = Solution()
print(s.productExceptSelf(nums))
