class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= len(nums)
        count = start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                nextIdx = (current + k ) % n
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                count += 1
                if start == current:
                    break
            start += 1