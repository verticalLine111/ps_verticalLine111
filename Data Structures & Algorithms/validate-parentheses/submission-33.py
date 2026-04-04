class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stk = []
        for i in range(len(s)):
            if s[i] in cto:
                if stk and stk[-1] == cto[s[i]]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(s[i])
        return len(stk) == 0