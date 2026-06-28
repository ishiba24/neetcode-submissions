# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #treat like regular addition, adding and then carrying over the leftover
        #keep a pointer for both
        c1 = l1
        c2 = l2
        res = []
        carry = 0
        dummy = ListNode()
        cur = dummy
        
        while c1 or c2:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            total = v1 + v2 + carry
            dig = total % 10
            cur.next = ListNode(dig)
            carry = total // 10
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
            cur = cur.next
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next
        