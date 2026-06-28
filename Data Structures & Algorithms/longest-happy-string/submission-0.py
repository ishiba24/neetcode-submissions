class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #maxHeap with elements, place the most freq element every time but check if the past two are of the same type
        #also need to check while countA < a, and so on
        maxHeap = []
        freqCount = {
            'a':a,
            'b':b,
            'c':c
        }
        for c, cnt in freqCount.items():
            if cnt:
                maxHeap.append([-cnt, c])
        heapq.heapify(maxHeap)
        s = ""
        while maxHeap:
            cnt, c = heapq.heappop(maxHeap)
            if len(s) > 1 and s[-1] == s[-2] == c:
                if not maxHeap:
                    break
                cnt2, c2 = heapq.heappop(maxHeap)
                s += c2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(maxHeap, [cnt2, c2])
                heapq.heappush(maxHeap, [cnt, c])
            else:
                    s += c
                    cnt += 1
                    if cnt:
                        heapq.heappush(maxHeap, [cnt, c])
        return s