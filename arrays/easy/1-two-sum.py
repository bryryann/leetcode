# Given an array of integers 'nums' and an integer 'target', 
# return indices of the two numbers such that they add up to 'target'.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    search = {}

    for i in range(len(nums)):
        if nums[i] in search:
            return [search[nums[i]], i]

        search[target - nums[i]] = i

    return []
