from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                sti, sth = stack.pop()
                w = (i - sti) * sth
                res = max(res, w)
                start = sti
            stack.append((start, h))

        for i,h in stack:
            res = max(res, (len(heights) - i) * h)
        return res