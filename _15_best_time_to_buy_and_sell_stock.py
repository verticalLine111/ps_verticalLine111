from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while l < len(prices) and r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res , profit)
                r+=1
            else:
                l = r
                r +=1
        return res