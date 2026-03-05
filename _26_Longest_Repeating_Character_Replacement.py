from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        smap = Counter()
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            smap[s[r]] += 1
            maxf = max(maxf , smap[s[r]])
            while r - l + 1 - maxf > k:
                smap[s[l]] -= 1
                l += 1
            res = max(res, len(s[l:r + 1]))

        return res