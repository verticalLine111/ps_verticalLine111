class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not self.isAN(s[l].lower()):
                l+=1
            if not self.isAN(s[r].lower()):
                r-=1
            if self.isAN(s[l].lower()) and self.isAN(s[r].lower()):
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
        return True
    def isAN(self, c: str) -> bool:
        if '0' <= c <= '9':
            return True
        if ord('a') <= ord(c) <= ord('z'):
            return True
        return False