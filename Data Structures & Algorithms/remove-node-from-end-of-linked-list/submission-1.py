# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers increment one n steps ahead so that second one lands on node to skip
        end = head
        dummy = ListNode()
        dummy.next = head
        left = dummy
        i = 0
        while i < n:
            end = end.next
            i += 1
        while end:
            end = end.next
            left = left.next
        left.next = left.next.next
        return dummy.next