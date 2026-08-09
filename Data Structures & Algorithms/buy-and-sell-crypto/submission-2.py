class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy day
        r = 1 # sell day
        maxP = 0

        while r < len(prices):
            # new profit with potential for a new max
            if prices[r] > prices[l]: 
                maxP = max(maxP, prices[r] - prices[l])
            # new lowest stock price, update buy day
            else:
                l = r
            
            # move r forward
            r += 1
        return maxP
