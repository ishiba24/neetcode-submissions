class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #must find the lowest weight capacity for all packages to be shipped in x amount of days
        #whats upper and lower bound? lower would be max(weights), upper would be sum(weights)?
        l, r = max(weights), sum(weights)
        res = r
        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
            