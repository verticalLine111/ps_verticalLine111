from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                sth, sti = stack.pop()
                w = i - sti
                max_area = max(max_area, w * sth)
                start = sti
            stack.append((h, start))

        for h, i in stack:
            w = len(heights) - i
            max_area = max(max_area, w * h)
        return max_area