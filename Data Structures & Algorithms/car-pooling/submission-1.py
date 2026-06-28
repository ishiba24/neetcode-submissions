class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sort/store in minHeap by starting location? seems more like interval question
        #keep a cap count and iterate, if cap + trips[0] > capacity return false
        points = []
        for passengers, start, end in trips:
            points.append([start, passengers])
            points.append([end, -passengers])
        points.sort()
        curPass = 0
        for point, passengers in points:
            curPass += passengers
            if curPass > capacity:
                return False
        return True