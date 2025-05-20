# Title: Valid Anagram
# ID: 242
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram
# Tags: hash table, string, sorting
# Runtime: 20ms, faster than only 5.12% of Python3 online submissions
# Memory Usage: 18.19mb, less than only 24.37% of Python3 online submissions

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chs = list(s)
        for c in t:
            if c not in chs:
                return False
            chs.remove(c)

        return True



s = Solution()
print(s.isAnagram('anagram', 'nagaram')) # True
print(s.isAnagram('rat', 'car')) # False
