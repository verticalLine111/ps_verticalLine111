from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        smap = Counter()
        res = 0
        for r in range(len(s)):
            smap[s[r]] += 1
            while smap[s[r]] > 1:
                smap[s[l]] -= 1
                l+= 1
            res = max(res, r - l + 1)
        return res