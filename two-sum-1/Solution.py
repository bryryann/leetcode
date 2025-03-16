from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in map:
                return [i, map[rem]]
            map[nums[i]] = i
        return []



print(Solution.twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(Solution.twoSum([3, 2, 4], 6))      # [1, 2]
print(Solution.twoSum([3, 3], 6))         # [0, 1]
