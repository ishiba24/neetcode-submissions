class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        seen = {}
        for i, v in enumerate(numbers):
            if (target - v) in seen:
                res.append(seen[target - v]+1)
                res.append(i+1)
                return res
            else:
                seen[v] = i

            
