class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res # does the xor, determines which number only appears once as if two nums are the same they result in 0.
        return res