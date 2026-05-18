class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while l < r:
            if heights[l] < heights[r]:
                sqr = (r - l) * heights[l]
                res = max(res, sqr)
                l+=1
            else:
                sqr = (r - l) * heights[r]
                res = max(res, sqr)
                r-=1
        return res
