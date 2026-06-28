class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # vertical binary search, then horizontal?
        l = 0
        r = len(matrix) - 1
        row = None
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0] :
                if target > matrix[m][-1]:
                    l = m + 1
                else:
                    row = matrix[m]
                    break
            else:
                return True
        if row == None:
            return False
        left , right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid - 1
            else:
                return True
        return False
            