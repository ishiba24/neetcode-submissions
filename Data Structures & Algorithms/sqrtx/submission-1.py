class Solution:
    def mySqrt(self, x: int) -> int:
        #use binary search from the range of numbers, if the floor equals x then its the sq root
        #can just use //, so multiply by itself and then // 1?
        l = 0
        r = x
        while l <= r:
            m = (l + r) // 2
            res = (m * m) // 1
            if res > x:
                r = m - 1
            elif res < x:
                l = m + 1
                ans = m
            else:
                return m 
        return ans