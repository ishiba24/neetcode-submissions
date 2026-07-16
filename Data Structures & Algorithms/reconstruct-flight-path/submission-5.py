class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Eulerian path, given a graph traverse each edge once
        #only add airport when no outgoing edges remain
        #sort tickets, pick smallest first
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        dfs('JFK')
        return res[::-1]