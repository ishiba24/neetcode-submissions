class Solution:
    def simplifyPath(self, path: str) -> str:
        #use a stack, and determine when to pop or append the directory
        cur = ''
        stack = []
        i = 0
        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != "" and cur !=".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)

