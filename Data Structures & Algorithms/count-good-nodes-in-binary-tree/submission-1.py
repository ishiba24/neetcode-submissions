# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs, but keep track of the maxVal along the path so far
        res = 0
        def dfs(node, maxVal):
            nonlocal res
            if not node:
                return 
            if node.val >= maxVal:
                res += 1
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        return res


