class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        res = 0
        while l < r:
            width = r - l
            if heights[l] < heights[r]:
                res = max(res , width * heights[l])
                l+=1
            else:
                res = max(res , width * heights[r])
                r-=1
        return res