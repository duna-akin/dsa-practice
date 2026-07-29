class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(prices[j] - prices[i], res)
        
        return res
            