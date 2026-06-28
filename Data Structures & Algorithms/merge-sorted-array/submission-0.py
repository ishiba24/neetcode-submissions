class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #shift each element to the right? fill from back since we have extra space, so we never overwrite elements
        i = m - 1
        j = n - 1
        last = m + n - 1 #last element in nums1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
