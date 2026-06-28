# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #BST so node are ordered
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if val < cur.val:
                if not cur.left:
                    newNode = TreeNode(val)
                    cur.left = newNode
                    break
                cur = cur.left
            elif val > cur.val:
                if not cur.right:
                    newNode = TreeNode(val)
                    cur.right = newNode
                    break
                cur = cur.right
            
        return root
            