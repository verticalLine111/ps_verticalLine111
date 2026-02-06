class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if self.isalnum(s[l].lower()) and self.isalnum(s[r].lower()):
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
            if not self.isalnum(s[l].lower()):
                l += 1
            if not self.isalnum(s[r].lower()):
                r -= 1
        return True

    def isalnum(self, c: str) -> bool:
        if ord('a') <= ord(c) <= ord('z'):
            return True
        elif '0' <= c <= '9':
            return True
        else:
            return False