class Solution:
    # mod by 10 each digit to access, then // by 10 to get next digit
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False

    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10 #slice off lsn
        return output

