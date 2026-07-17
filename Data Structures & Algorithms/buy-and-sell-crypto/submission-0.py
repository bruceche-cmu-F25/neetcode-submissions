class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            left = i
            right = len(prices) - 1
            profit = 0
            while left < right:
                profit = prices[right] - prices[left]
                maxprofit = max(profit, maxprofit)
                right -= 1
        return maxprofit
            
            