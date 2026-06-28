class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #area = len * width
        res = 0
        stack = [] #ind, h
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                res = max(res, height * (i - ind))
                start = ind
            stack.append((start, h))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res

        