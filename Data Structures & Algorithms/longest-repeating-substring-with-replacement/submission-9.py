class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap = {}
        maxf = 0
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in fmap:
                fmap[s[r]] += 1
            else:
                fmap[s[r]] = 1
            maxf = max(maxf, fmap[s[r]])
            while (r - l + 1) - maxf > k:
                fmap[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res