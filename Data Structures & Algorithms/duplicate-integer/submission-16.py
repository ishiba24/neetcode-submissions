class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        charDict = {}
        for i in nums:
            if i not in charDict:
                charDict[i] = 1
            elif i in charDict:
                return True
        return False