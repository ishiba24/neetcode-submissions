# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # seems like we just do the same reverse technique but in between the bounds
        dummy = ListNode(0, head)
        beforeLeft = dummy
        for _ in range(left - 1):
            beforeLeft = beforeLeft.next
        cur = beforeLeft.next
        #now at start
        afterRight = cur
        for _ in range(right - left + 1):
            afterRight = afterRight.next
        prev = afterRight
        #how can i point 1 to 4?
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        beforeLeft.next = prev
        return dummy.next