class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        smap = {}
        for r in range(len(s)):
            c = s[r]
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
            while smap[c] > 1:
                smap[s[l]] -= 1
                l +=1
            res = max(res , r-l+1)
        return res