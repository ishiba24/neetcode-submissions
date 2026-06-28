class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #greedy solution, notice that each time a price goes up we should buy and then sell
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i-1])
        return profit