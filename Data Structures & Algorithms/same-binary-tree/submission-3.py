# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #keep two pointers and do inorder traversal, return true if always same else false
        qQueue = deque([q])
        pQueue = deque([p])
        while pQueue and qQueue:
            for _ in range(len(pQueue)):
                q = qQueue.popleft()
                p = pQueue.popleft()
                if q is None and p is None:
                    continue
                if p is None or q is None or p.val != q.val:
                    return False
                qQueue.append(q.left)
                qQueue.append(q.right)
                pQueue.append(p.left)
                pQueue.append(p.right)
        return True

