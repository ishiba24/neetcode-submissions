class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #from 1/2 to 1/3 of the time, any way to do voting algo
        count = defaultdict(int)
        total = len(nums)
        res = []
        for num in nums:
            count[num] += 1
        for num in count:
            if count[num] > total // 3:
                res.append(num)
        return res
