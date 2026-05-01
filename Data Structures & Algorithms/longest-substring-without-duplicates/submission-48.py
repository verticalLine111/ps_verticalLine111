class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in mp and mp[s[r]] > 0:
                mp[s[l]] -= 1
                l+= 1
            mp[s[r]] = 1
            res = max(res , r - l + 1)
        return res