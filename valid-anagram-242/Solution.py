class Solution:

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs = list(s)
        for c in t:
            if c not in cs:
                return False
            cs.remove(c)

        return True


print(Solution.isAnagram("anagram", "nagaram"))
print(Solution.isAnagram("rat", "car"))
