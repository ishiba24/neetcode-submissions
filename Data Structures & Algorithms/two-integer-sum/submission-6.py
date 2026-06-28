class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tMap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in tMap:
                return sorted([tMap[diff], i])
            tMap[v] = i