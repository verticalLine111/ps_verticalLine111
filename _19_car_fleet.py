from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ziplist = list(zip(position, speed))
        ziplist.sort(reverse=True)
        for p, s in ziplist:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)