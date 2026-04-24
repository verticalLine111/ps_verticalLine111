class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        cto = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for i in range(len(s)):
            if s[i] in cto:
                if stk and stk[-1] == cto[s[i]]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(s[i])
        if len(stk) == 0:
            return True
        else:
            return False
