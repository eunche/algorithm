from typing import List

"""
-투 포인터
Runtime:  844 ms
Memory:  17.4 MB

특징: -첫번째 for문과 중복값 건너뛰기 까지는 브루트 포스 알고리즘과 같지만, 그 이후 비교해야 할
       값이 2개로 줄어들어, 투 포인터를 활용한게 핵심.
      -sum==0일때 left+1 right-1 하는 이유는, 하나만 움직여봤자 0이 될 수 없으므로 둘 다 움직여야 한다.
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

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
