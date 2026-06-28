class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #so at each point you can either add a matchstick or skip it, but you need to make a total of 4 counts
        #if you can ever make the 4 then you return true, else false
        #at each point you either start a new side, add the current matchstick, maybe sort by descending order?
        #at each point add it to one of 4 sides
        target = sum(matchsticks) // 4
        s1, s2, s3, s4 = 0,0,0,0
        matchsticks.sort(reverse=True)
        def backtrack(i):
            nonlocal s1
            nonlocal s2
            nonlocal s4
            nonlocal s3
            #print(s1, s2, s3, s4)
            if s1 > target or s2 > target or s3 > target or s4 > target:
                    return False
            if i >= len(matchsticks):
                if s1 == s2 == s3 == s4 and s1 == target:
                    return True
                return False
            s1 += matchsticks[i]
            if backtrack(i + 1):
                return True
            s1 -= matchsticks[i]
            s2 += matchsticks[i]
            if backtrack(i + 1):
                return True
            s2 -= matchsticks[i]
            s3 += matchsticks[i]
            if backtrack(i + 1):
                return True
            s3 -= matchsticks[i]
            s4 += matchsticks[i]
            if backtrack(i + 1):
                return True
            s4 -= matchsticks[i]
            return False
        return backtrack(0)
