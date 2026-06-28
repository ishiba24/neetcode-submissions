class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #can solve in O(n) using hashmap count
        #O(1) using boyer moore algo
        res = 0
        count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res