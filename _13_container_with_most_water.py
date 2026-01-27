from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0 
        r = len(heights) -1
        while l < r :
            square = min(heights[l] , heights[r]) * (r-l)
            res = max(res, square)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res