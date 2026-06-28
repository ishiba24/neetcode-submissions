class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #think of it like a graph problem, and try to detect a cycle. if theres a cycle, than its impossible to take the class(no starting point)
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


