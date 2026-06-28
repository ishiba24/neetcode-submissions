class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(opn, cls):
            if opn == cls == n:
                 res.append("".join(stack))
                 return
            if opn < n:
                stack.append("(")
                backtrack(opn + 1, cls)
                stack.pop()
            if cls < opn:
                stack.append(")")
                backtrack(opn, cls + 1)
                stack.pop()
        backtrack(0,0)
        return res