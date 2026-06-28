class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #need a minHeap sorted by processingtime
        #so append the enq, proc, and index to minHeap, sort it by processing time, maybe use a q and add to minHeap when time passes 
        indexedTasks = []
        for i, task in enumerate(tasks):
            enqueueTime, processingTime = task
            indexedTasks.append([enqueueTime, processingTime, i])
        minHeap = []
        indexedTasks.sort()
        res = []
        time = 0
        i = 0
        n = len(tasks)
        while i < n or minHeap:
            if not minHeap and time < indexedTasks[i][0]:
                time = indexedTasks[i][0]
            while i < n and indexedTasks[i][0] <= time:
                enqueueTime, processingTime, index = indexedTasks[i]
                heapq.heappush(minHeap, [processingTime, index])
                i += 1
            processingTime, index = heapq.heappop(minHeap)
            time += processingTime
            res.append(index)
        return res