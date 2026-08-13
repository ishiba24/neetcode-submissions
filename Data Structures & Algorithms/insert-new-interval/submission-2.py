class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #may have to merge overlapping. need to check if end of interval is > start of next, in that case they can merge and the start of first and end of last is the new interval
        if not intervals:
            return [newInterval]
        n = len(intervals)
        target = newInterval[0]
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if intervals[m][0] < target:
                l = m + 1
            else:
                r = m -1
        intervals.insert(l, newInterval)
        #now merge intervals pass
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res