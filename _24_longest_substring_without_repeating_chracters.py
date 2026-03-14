class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in smap:
                smap[s[r]] += 1
            else:
                smap[s[r]] = 1
            while smap[s[r]] > 1:
                smap[s[l]] -= 1
                l += 1
            res = max(res ,r-l+1)
        return res