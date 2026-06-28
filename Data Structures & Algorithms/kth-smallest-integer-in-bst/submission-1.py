# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal,  
        res = 0
        cnt = 0
        def dfs(node):
            nonlocal cnt
            nonlocal res
            if not node:
                return
            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
            if res:
                return
            dfs(node.right)
        dfs(root)
        return res