class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = v1 + v2
                stack.append(v2)
                stack.append(v1)
                stack.append(v3)
            elif op == "C":
                stack.pop()
            elif op == "D":
                val = stack.pop()
                stack.append(val)
                stack.append(val * 2)
            else:
                stack.append(int(op))
        return sum(stack)