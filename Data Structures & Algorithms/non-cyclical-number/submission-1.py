class Solution:
    # mod by 10 each digit to access, then // by 10 to get next digit
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        if fast == 1:
            return True
        else:
            return False


    def sumOfSquares(self, n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n// 10
        return output

        #same as LL cycle detection, except you build the number yourself through sum of squares.

