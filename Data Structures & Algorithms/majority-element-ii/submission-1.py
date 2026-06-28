class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #from 1/2 to 1/3 of the time, any way to do voting algo
        #o(n) space, o(n) time
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) <= 2:
                continue
            newCount = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    newCount[num] = c - 1
            count = newCount
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res
