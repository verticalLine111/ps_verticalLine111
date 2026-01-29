from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        i = 0
        j = i + 1
        while i < len(prices) and  j <= len(prices) - 1:
            if prices[i] >= prices[j]: # is profit
                i = j
                j = i + 1
            else:
                while prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    maxP = max(maxP, profit)
                    j += 1
                    if j > len(prices) -1:
                        break
        return maxP