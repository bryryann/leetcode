# Title: Contains Duplicate
# ID: 217
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate
# Tags: array, hash table, sorting
# Runtime: 15ms, faster than 41.39% of Python3 online submissions
# Memory Usage: 31.46mb, less than 83.01% of Python3 online submissions

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()

        for n in nums:
            if n in hash:
                return True
            hash.add(n)

        return False


s = Solution()
print(s.containsDuplicate([1,2,3,1])) # true
print(s.containsDuplicate([1,2,3,4])) # false
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # true
