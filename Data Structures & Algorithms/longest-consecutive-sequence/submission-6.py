class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use a hashset, only start counting if nums -1 not in set
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest