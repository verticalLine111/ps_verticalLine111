from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        smap = Counter()
        res = 0
        for r in range(len(s)):
            smap[s[r]] += 1
            maxf = max(maxf, smap[s[r]])
            while r - l + 1 - maxf > k:
                smap[s[l]] -= 1
                l+=1
            res = max(res, r-l + 1)
        return res