from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        smap = Counter()
        need = len(tmap)
        have = 0
        l = 0
        res = s + '!'
        for r in range(len(s)):
            smap[s[r]] += 1
            if s[r] in smap and smap[s[r]] == tmap[s[r]]:
                have += 1

            while have == need:
                current = s[l:r + 1]
                res = min(res, current, key=len)
                smap[s[l]] -= 1
                if s[l] in smap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1

        if len(res) > len(s):
            return ""
        return res