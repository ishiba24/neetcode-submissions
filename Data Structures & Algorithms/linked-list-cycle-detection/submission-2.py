# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #cycle detection algo, have one increment by one and the other inc by two. if they hit the same node they overlap
        cur1 = head
        cur2 = head
        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
        return False