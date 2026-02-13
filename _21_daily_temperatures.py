from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                sti, stt = stack.pop()
                res[sti] = i - sti
            stack.append((i , t))
        return res