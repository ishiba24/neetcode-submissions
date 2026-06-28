class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #keep a window of k closest elements, for each new element if it is added then remove old element?
        #only add if it is less than l's dist, if tied keep l
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if abs(x - arr[m]) > abs(arr[m + k] - x):
                l = m + 1
            else:
                r = m
        return arr[l: l + k]