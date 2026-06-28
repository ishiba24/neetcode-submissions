class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer approach, keep a max of water. water = dist(l,r) * max(l,r).
        #how to iterate left? 
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(heights[r], heights[l]))
            if heights[l] < heights[r]:
                l += 1
            else: r -= 1
        return area