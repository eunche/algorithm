from typing import List

"""
실패

내 생각: 2개라면 포인터 풀이를 했을텐데, 3개여서 3중포문을 쓰면 시간초과가 뜰 것 같아 다른 해결책이 떠오르지 않았다.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums의 요소가 3개보다 적을시 -> return []
        if len(nums) < 3:
            return []

        result = []
        left, right = 0, len(nums) - 1

        # 정렬 [-4, -1, -1, 0, 1, 2]
        nums.sort()

        pointer = right - 1
        while left != right - 1:
            pointer = right - 1

            # 왼쪽값이 양수이면 -> break
            if nums[left] > 0:
                break

            # 합이 음수이면 -> left += 1
            if nums[left] + nums[pointer] + nums[right] < 0:
                left += 1
                continue

            while left != right - 1:
                if nums[left] + nums[pointer] + nums[right] == 0:
                    result.append([nums[left], nums[pointer], nums[right]])
                pointer -= 1

            right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
