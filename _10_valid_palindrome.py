class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        lower = s.lower()
        while l <= r:
            if self.isAN(lower[l]) and self.isAN(lower[r]):
                if lower[l] != lower[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            else:
                if not self.isAN(lower[l]):
                    l += 1
                if not self.isAN(lower[r]):
                    r -= 1
        return True

    def isAN(self, c:str) -> bool:
        if ord('a') <= ord(c) <= ord('z'):
            return True
        if '0' <= c <= '9':
            return True
        return False