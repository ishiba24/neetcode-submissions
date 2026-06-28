class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #just hold k elements, maxHeap so we just return the very front
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        print(maxHeap)
        return -maxHeap[0]