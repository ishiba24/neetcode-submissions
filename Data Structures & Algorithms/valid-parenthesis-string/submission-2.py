class Solution:
    def checkValidString(self, s: str) -> bool:
        #count how many ( and how many *, if the difference is too great then return false?
        leftMin, leftMax = 0,0 
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax <0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
            
