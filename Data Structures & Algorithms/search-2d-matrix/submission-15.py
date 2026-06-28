class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # 1) Binary search to find the correct row
        l, r = 0, len(matrix) - 1
        row = None

        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = matrix[m]
                break

        if row is None:
            return False

        # 2) Binary search within the row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
            else:
                return True

        return False
                