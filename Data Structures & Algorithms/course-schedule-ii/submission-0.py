class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #treat like a graph, maybe map each in a hashMap? then keep an ordered output by doing >/<
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        output = []
        cycle, vis = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in vis:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            vis.add(course)
            output.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output