class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
       #total worth is prof + capital, but you need a minimum of w capital to start a task. sort using maxHeap by total cap, and then see if you have the minimal cap to start it?
        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                cap, prof = projects[i]
                heapq.heappush(maxHeap, -prof)
                i += 1
            if not maxHeap:
                break
            prof = heapq.heappop(maxHeap)
            w += -prof
        return w