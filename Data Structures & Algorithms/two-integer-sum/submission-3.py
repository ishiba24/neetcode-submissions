class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          prevMap={}
          for i,v in enumerate(nums):
            diff=target-v
            if diff in prevMap:
                return sorted([i,prevMap[diff]])
            prevMap[v]=i

            

