class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #slow, fast pointers? if the two are ever the same they will hit no? but end check is slow not the fast ptr
        #have fast ptr wrap around
        slow, fast = 0, 0
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