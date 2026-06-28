class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur = intervals[i]
            lastMerged = res[-1]
            if cur[0] <=lastMerged[1]:
                lastMerged[1] = max(cur[1], lastMerged[1])
            else:
                res.append(cur)
        return res