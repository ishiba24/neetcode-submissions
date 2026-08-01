class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        prev3, prev2, prev1 = 0, 1, 1
        for curVal in range(3, n + 1):
            cur = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = cur
        return prev1
