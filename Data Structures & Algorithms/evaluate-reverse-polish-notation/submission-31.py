class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                a,b = stk.pop(), stk.pop()
                stk.append(a+b)
            elif tokens[i] == '-':
                a,b = stk.pop() , stk.pop()
                stk.append(b - a)
            elif tokens[i] == '*':
                a,b = stk.pop(), stk.pop()
                stk.append(a * b)
            elif tokens[i] == '/':
                a,b = stk.pop(), stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(tokens[i]))
        return stk[0]