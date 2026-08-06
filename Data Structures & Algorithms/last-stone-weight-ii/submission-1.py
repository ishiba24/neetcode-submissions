class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for curSum in range(target, stone - 1, -1):
                if dp[curSum - stone]:
                    dp[curSum] = True
        for subsetSum in range(target, -1, -1):
            if dp[subsetSum]:
                return total - 2* subsetSum