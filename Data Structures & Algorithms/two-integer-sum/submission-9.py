class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in numHash:
                return [numHash[needed], i]
            numHash[num] = i