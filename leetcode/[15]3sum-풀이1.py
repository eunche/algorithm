from typing import List

"""
-브루트 포스(3중for문)
Runtime: 시간초과
Memory:   MB

특징: results 리스트에 중복값을 허용하지 않아서, 3중for문에서 중복 제거 처리를 한게 핵심
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 브루트 포스 n^3 반복
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
