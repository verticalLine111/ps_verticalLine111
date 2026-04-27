class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cnt = {}
        for r in range(len(s)):
            if s[r] in cnt:
                l = max(cnt[s[r]] + 1 , l)
            cnt[s[r]] = r
            res = max(res, r - l + 1)
        return res