from typing import List

"""
Runtime: 52 ms
Memory: 14.5 MB

특징: 딕셔너리(해시 테이블)의 조회는 평균적으로 O(1)이므로 전체 시간복잡도는 O(n)이 된다.
      (*LeetCode에선 실행속도가 풀이1보다 크게 나온다..)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


s = Solution()

nums = [0, 4, 3, 0]
target = 0
print(s.twoSum(nums, target))
