from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        r = 1
        while l < len(prices):
            if r >= len(prices):
                break
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
                r += 1
            elif prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r +=1

        return maxP