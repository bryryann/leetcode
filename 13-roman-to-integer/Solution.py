class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        for i in range(len(s)-1):
            if nums[s[i]] < nums[s[i+1]]:
                total -= nums[s[i]]
            else:
                total += nums[s[i]]
        return total + nums[s[-1]]


sol = Solution()
print(sol.romanToInt("III")) # 3
print(sol.romanToInt("LVIII")) # 58
print(sol.romanToInt("MCMXCIV")) # 1994
