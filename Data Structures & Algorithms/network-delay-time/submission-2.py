class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #use dijkstras from the source node, then just return the minimum time until all nodes are in vis?
        adj = defaultdict(list)
        minHeap = [(0, k)]
        vis = set()
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        maxDist = 0
        while minHeap:
            for i in range(len(minHeap)):
                dist, node = heapq.heappop(minHeap)
                if node in vis:
                    continue
                vis.add(node)
                maxDist = max(maxDist, dist)
                for nei in adj[node]:
                    print(nei[0])
                    if nei[0] not in vis:
                        heapq.heappush(minHeap, (dist + nei[1], nei[0]))
        print(len(vis))
        return maxDist if len(vis) == n else -1

            