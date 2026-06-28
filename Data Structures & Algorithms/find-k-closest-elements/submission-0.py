class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #keep a window of k closest elements, for each new element if it is added then remove old element?
        #only add if it is less than l's dist, if tied keep l
        res = []
        l = 0
        count = k
        for r in range(len(arr)):
            if count > 0:
                res.append(arr[r])
                count -= 1
            else:
                if abs(arr[r] - x) < abs(arr[l] - x):
                    res.pop(0)
                    res.append(arr[r])
                    l += 1
        return res