# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #find root by looking at where inorder and preorder cross
        indices = {val: idx for idx, val in enumerate(inorder)}
        preIdx = 0
        def dfs(l, r):
            nonlocal preIdx
            if l > r:
                return None
            rootVal = preorder[preIdx]
            preIdx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)
                
            