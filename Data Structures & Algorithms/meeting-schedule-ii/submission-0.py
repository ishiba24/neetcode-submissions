"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #now we need to count how many conflicts there are, and return this number
        intervals.sort(key=lambda i:i.start)
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)
