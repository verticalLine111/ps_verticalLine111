def isPalindrome( s: str) -> bool:
    l = 0
    r = len(s) -1
    ls = s.lower()
    print(s[0])
    while l < r:
        if isAlphnumeric(ls[l]) and isAlphnumeric(ls[r]):        
            if ls[r] != ls[l]:
                return False
            l += 1
            r -= 1
        else:
            if not isAlphnumeric(ls[l]):
                l += 1
            if not isAlphnumeric(ls[r]):
                r-=1
    return True

def isAlphnumeric( s: str):
    return ((ord(s) <= ord('z')) and (ord(s) >= ord('a'))) or ('0' <= s and s <= '9')

res = isPalindrome(s = "ab")
print(res)