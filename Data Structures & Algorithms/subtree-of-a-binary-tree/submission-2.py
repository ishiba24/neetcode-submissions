# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSubtree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return checkSubtree(p.left, q.left) and checkSubtree(p.right, q.right)
            else:
                return False
        def dfs(root, subRoot):
            if not root:
                return
            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)
            if left or right:
                return True
            if root.val == subRoot.val:
                subtree = checkSubtree(root, subRoot)
                if subtree:
                    return True
            return False
        return dfs(root, subRoot)

            
            
            