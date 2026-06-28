# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #lvl order traversal but just append the last node at each time
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                furthestRight = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(furthestRight.val)
        return res
        