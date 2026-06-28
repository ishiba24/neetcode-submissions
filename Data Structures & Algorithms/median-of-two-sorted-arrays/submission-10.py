class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #try to partition the two arrays, and find the valid partition through binary search. min(right) < max(left) and vice versa.
        #take max from left and min from right, add and // by 2.
        #take max of left a and b partition, and min of right a and b partition.
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        if len(a) > len(b):
            a, b = b, a
        l, r = 0, len(a) -1
        while True:
            i = (l + r) // 2 #a
            j = half - i - 2 #b

            aLeft = a[i] if i >= 0 else float('-inf')
            aRight = a[i + 1] if (i + 1) < len(a) else float('inf')
            bLeft = b[j] if j >= 0 else float('-inf')
            bRight = b[j + 1] if j + 1 < len(b) else float('inf')

            if aLeft <= bRight and aRight >= bLeft:
                if total % 2 == 0: #even
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight: #left partition too big
                r = i - 1
            else:
                l = i + 1


