# Title: Two Sum
# ID: 1
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum
# Tags: array, hash table
# Runtime: <20ms, faster than 100.0% of Python3 online submissions
# Memory Usage: 18.88mb, less than 51.06% of Python3 online submissions

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in m:
                return [m[rem], i]
            m[nums[i]] = i
        return []


s = Solution()
print(s.twoSum([2,7,11,15], 9)) # [0,1]
print(s.twoSum([3,2,4], 6)) # [1,2]
print(s.twoSum([3,3], 6)) # [0,1]

