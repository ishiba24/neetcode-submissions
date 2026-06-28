class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #if you hit right border, move down, hit bottom, move left, hit left, move up
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]