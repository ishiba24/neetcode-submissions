class Solution:
    def getSum(self, a: int, b: int) -> int:
        #how to handle neg? pos can just or
        carry = 0
        res = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            curBit = aBit ^bBit ^ carry
            carry = (aBit + bBit + carry) >= 2
            if curBit:
                res |= (1 << i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res