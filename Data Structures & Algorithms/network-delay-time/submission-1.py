class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstras algo since edges are weighted, use a minheap
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)] #pathlen, node
        vis = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in vis:
                continue #if node alr visited, continue
            vis.add(n1)
            t = w1 #time

            for n2, w2 in edges[n1]:
                if n2 not in vis:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(vis) == n else -1
