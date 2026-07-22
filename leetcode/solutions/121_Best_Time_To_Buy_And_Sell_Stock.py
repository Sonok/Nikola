
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        # montonically decreasing? you only care about the smallest number u've seen so far

        lowest = 10 ** 4 + 1 # highest possible price
        for i in range(n):
            maxProfit = max(prices[i] - lowest, maxProfit) # so we see best ROI based on curr price and lowest price seen so far 
            lowest = min(lowest, prices[i])
        
        return maxProfit
