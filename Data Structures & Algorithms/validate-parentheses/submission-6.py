class Solution:
    def isValid(self, s: str) -> bool:
        #keep a stack of open parentheses so far, if we run into a close and it matches then pop, else false
        stack = []
        closeToOpen = {')':'(', '}':'{', ']': '['}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True
                