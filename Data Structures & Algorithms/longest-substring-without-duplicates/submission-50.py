class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fmap = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in fmap:
                fmap[s[r]] += 1
            else:
                fmap[s[r]] = 1
            while fmap[s[r]] > 1:
                fmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res