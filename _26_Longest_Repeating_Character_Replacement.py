from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        smap = Counter()
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in smap:
                smap[s[r]] += 1
            else:
                smap[s[r]] = 1
            maxf = max(maxf, smap[s[r]])

            while r - l + 1 - maxf > k:
                smap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res