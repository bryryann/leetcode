from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = set()

        for n in nums:
            if n in k:
                return True
            k.add(n)

        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1])) # true
print(s.containsDuplicate([1, 2, 3, 4])) # false
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true

