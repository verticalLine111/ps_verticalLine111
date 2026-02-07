class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for p in s:
            if p in ')}]':
                if len(stack) > 0 and closeToOpen[p] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(p)

        if len(stack) > 0:
            return False

        return True