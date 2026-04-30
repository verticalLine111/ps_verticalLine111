class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mp = {}
        maxk = 0
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                mp[s[r]] += 1
            else:
                mp[s[r]] = 1
            maxk = max(maxk, mp[s[r]])
            while r - l + 1 - maxk > k:
                mp[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
            
        return res