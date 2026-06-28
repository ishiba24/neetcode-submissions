class MedianFinder:

    def __init__(self):
        self.leftHalf = []
        self.rightHalf = []

    def addNum(self, num: int) -> None:
        if self.leftHalf and num > -self.leftHalf[0]:
            heapq.heappush(self.rightHalf, num)
        else:
            heapq.heappush(self.leftHalf, -num)
        if len(self.rightHalf) > len(self.leftHalf) + 1:
            val = heapq.heappop(self.rightHalf)
            heapq.heappush(self.leftHalf, -val)
        if len(self.leftHalf) > len(self.rightHalf) + 1:
            val = -heapq.heappop(self.leftHalf)
            heapq.heappush(self.rightHalf, val)

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            return ((-self.leftHalf[0] + self.rightHalf[0]) / 2.0)
        
        