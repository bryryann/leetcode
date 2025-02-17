class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prev = strs[0]
        p_len = len(prev)

        for s in strs[1:]:
            while prev != s[0:p_len]:
                if p_len == 0:
                    return ""

                p_len -= 1
                prev = prev[0:p_len]

        return prev



sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"])) # "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"])) # ""
print(sol.longestCommonPrefix(["abracadabra", "abraham", "abracate"])) # ""
print(sol.longestCommonPrefix(["ab", "a"]))
