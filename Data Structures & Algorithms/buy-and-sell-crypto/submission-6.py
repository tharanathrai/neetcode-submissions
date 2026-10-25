class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minBuy = 0, prices[0]

        for price in prices:
            maxP = max(maxP, price - minBuy)
            minBuy = min(minBuy, price)

        return maxP