"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #how can we handle random pointers? two passes is first instinct, 
        OldToCopy = {None: None}
        dummy = head
        while dummy:
            copy = Node(dummy.val)
            OldToCopy[dummy] = copy
            dummy = dummy.next
        cur = head
        while cur:
            copy = OldToCopy[cur]
            copy.next = OldToCopy[cur.next]
            copy.random = OldToCopy[cur.random]
            cur = cur.next
        return OldToCopy[head]