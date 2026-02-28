from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ziplist = list(zip(position, speed))
        ziplist.sort(reverse=True)
        stack = []
        for p, s in ziplist:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)