# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #use a hashmap to map the index to the node 
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.preIdx = 0
        def dfs(l, r):
            if l > r:
                return None
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)