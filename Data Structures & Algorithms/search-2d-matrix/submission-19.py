class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first find the right row, then binary search that row
        curRow = []
        rows, cols = len(matrix), len(matrix[0])
        for row in matrix:
            if row[-1] == target:
                return True
            if row[-1] < target:
                continue
            elif row[-1] > target:
                curRow = row
                break
        if not curRow:
            return False
        l, r = 0, len(curRow) - 1
        while l <= r:
            m = (l + r) //2
            if curRow[m] > target:
                r = m - 1
            elif curRow[m] < target:
                l = m + 1
            else:
                return True
        return False