class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #can calculate the target value, see if it exists in hashmap yet
        vtoI = defaultdict(int)
        for i, v in enumerate(nums):
            newTar = target - v
            if newTar in vtoI:
                return [vtoI[newTar], i]
            vtoI[v] = i
        return [vtoI[newTar], i]
        

