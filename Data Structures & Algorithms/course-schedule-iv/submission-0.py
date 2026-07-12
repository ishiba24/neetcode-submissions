class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses
        adjList = defaultdict(list)
        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        nodePrereq = defaultdict(set)
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                nodePrereq[nei].add(node)
                for prereq in nodePrereq[node]:
                    nodePrereq[nei].add(prereq)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        res = []
        for q in queries:
            res.append(q[0] in nodePrereq[q[1]])
        return res