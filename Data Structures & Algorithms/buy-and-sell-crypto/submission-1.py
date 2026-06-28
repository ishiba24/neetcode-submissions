class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        l=0
        r=1
        while r<len(prices):
            maxP=max(maxP,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
            r+=1
        return maxP

