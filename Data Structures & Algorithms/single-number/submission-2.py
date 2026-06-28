class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR since two identical numbers will cancel out
        res = 0
        for num in nums:
            res = res^num #XOR, if identical = 0, if only 1 remains the same
        return res