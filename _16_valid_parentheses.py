class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) > 0 and stack.pop() == '(':
                    continue
                else:
                    return False
            if s[i] == '}':
                if len(stack) > 0 and stack.pop() == '{':
                    continue
                else:
                    return False
            if s[i] == ']':
                if len(stack) > 0 and stack.pop() == '[':
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False

        return True