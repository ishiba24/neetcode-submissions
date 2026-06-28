class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a heap, continue to pop the element which appears the most?
        #use minheap, store k most freq elements by appending a (el, freq)
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        minHeap = []
        for num, count in freqMap.items():
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        for i in range(k):
            count, num = (heapq.heappop(minHeap))
            res.append(num)
        return res