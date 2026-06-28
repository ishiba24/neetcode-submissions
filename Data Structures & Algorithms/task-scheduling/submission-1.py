class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #need to do some type of maxHeap, use a freqArray and append to the maxHeap the elements with the highest freq?
        #always do the task with highest frequency? use a queue and append none when cpu needs to be idle
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
