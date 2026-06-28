# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #need to use bfs
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            newList = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    newList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if newList:
                res.append(newList)
        return res
