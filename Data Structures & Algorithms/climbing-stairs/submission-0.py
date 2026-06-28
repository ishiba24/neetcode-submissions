class Solution:
    def climbStairs(self, n: int) -> int:
        #n is the number of steps, can either travel 1 or 2 steps each time. recursively call the different paths?
        #create a memo dict that maps the number you're on to the different ways you can achieve it?
        cache = [-1] * n

        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)