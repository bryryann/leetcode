# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    s = set()
    for n in nums:
        if n in s:
            return True
        s.add(n)

    return False

