class Solution:
    def trap(self, height: List[int]) -> int:
        #water held is the min(l, r), diff at each block. 
        l, r = 0, len(height) - 1
        leftMax = height[0]
        rightMax = height[len(height) - 1]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res