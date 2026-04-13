class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stk = []
        for i in range(len(s)):
            if stk and s[i] in cto and stk[-1] == cto[s[i]] :
                stk.pop()
            else:
                stk.append(s[i])
        if len(stk) > 0:
            return False
        return True