class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mP = 0
        b = 0
        s = 1
        while s < len(prices):
            if prices[b] < prices[s]:
                mP = max(mP, prices[s] - prices[b])
            else:
                b = s
            s += 1
        return mP