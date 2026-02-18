from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+':
                a,b = stk.pop(), stk.pop()
                stk.append(a+b)
            elif t in '-':
                a, b= stk.pop(), stk.pop()
                stk.append(b-a)
            elif t in '*':
                a,b = stk.pop(), stk.pop()
                stk.append(a*b)
            elif t in '/':
                a, b = stk.pop(), stk.pop()
                stk.append(int (b / a))
            else:
                stk.append(int(t))
        return stk[0]