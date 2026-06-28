class Solution:
    def rob(self, nums: List[int]) -> int:
        #cant rob two houses next to each other.
        rob1, rob2 = 0, 0
        for curVal in nums:
            newVal = max(curVal + rob1, rob2) #rob1 is 2 back, rob2 is 1 back
            rob1 = rob2
            rob2 = newVal

        return rob2