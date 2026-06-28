"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x, y, size):
            if size == 1:
                return Node(grid[x][y] == 1, True)
            half = size // 2
            topLeft = build(x,y,half)
            topRight = build(x, y + half, half)
            bottomLeft = build(x + half, y, half)
            bottomRight = build(x + half, y + half, half)
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf):
                if topLeft.val == topRight.val==bottomRight.val==bottomLeft.val:
                    return Node(topLeft.val, True)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        return build(0,0, len(grid))