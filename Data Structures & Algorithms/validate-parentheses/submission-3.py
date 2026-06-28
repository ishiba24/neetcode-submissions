class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        CtoO={")":"(","}":"{","]":"["}
        stack=[]
        for char in s:
            if char in CtoO:
                if stack and stack[-1]==CtoO[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True