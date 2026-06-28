class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        n = len(stones)

        while len(stones) > 1:
            v1 = heapq.heappop(stones)
            v2 = heapq.heappop(stones)
            if v1 == v2:
                continue
            heapq.heappush(stones, v1 - v2)
        stones.append(0)
        return abs(stones[0]) if stones else 0