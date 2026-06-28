class Solution:
    def reorganizeString(self, s: str) -> str:
        #freqMap, then maxHeap that puts the max element down each time and appends -1
        count = Counter(s)
        maxHeap = []
        for c, cnt in count.items():
            maxHeap.append([-cnt, c])
        heapq.heapify(maxHeap)
        res = ""
        prev = None
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            res += c
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, c]
        if prev:
            return ""
        return res

