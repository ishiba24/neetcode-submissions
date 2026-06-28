class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if pick[i]:
                    continue
                cur.append(nums[i])
                pick[i] = True
                backtrack(cur)
                cur.pop()
                pick[i] = False

        backtrack([])
        return res