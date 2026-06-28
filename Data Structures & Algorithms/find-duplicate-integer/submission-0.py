class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 #dist(intersection -> start of cycle) == dist(start ->start of cycle)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow