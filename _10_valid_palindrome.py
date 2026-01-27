class Solution:
    # "Was it a car or a cat I saw?"
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if self.isAN(s[l]) and self.isAN(s[r]):
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
            else:
                if not self.isAN(s[l]) and self.isAN(s[r]):
                    l+=1
                if self.isAN(s[l]) and not self.isAN(s[r]):
                    r -= 1
                if  not self.isAN(s[l]) and not self.isAN(s[r]):
                    l+=1
                    r-=1


        return True
    def isAN(self, c: str) -> bool:
        return (ord('a')<= ord(c) and ord(c) <= ord('z')) or (ord('A') <= ord(c) and ord(c) <=ord('Z')) or ('0' <= c and c <= '9')