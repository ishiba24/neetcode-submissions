class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target==matrix[i][0]:
                return True
            if target<matrix[i][0]:
                sub=matrix[i-1]
                break
            if len(matrix)==1 or i==len(matrix)-1:
                sub=matrix[i]
                break
            
        l=0
        r=len(sub)-1
        while l<=r:
            m=(l+r)//2
            if sub[m]<target:
                l=m+1
            elif sub[m]>target:
                r=m-1
            else:
                return True
        return False
