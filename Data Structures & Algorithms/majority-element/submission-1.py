class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #use a voting algorithm, iterate through and one will survive
        finalNum = 0
        count = 0
        for num in nums:
            if finalNum == num:
                count += 1
            else:
                count -= 1
            if count <= 0:
                finalNum = num
                count = 1
        return finalNum