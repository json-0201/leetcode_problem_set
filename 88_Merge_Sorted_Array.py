class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        a, b, ind = m-1, n-1, m+n-1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[ind] = nums1[a]
                a -= 1
            else:
                nums1[ind] = nums2[b]
                b -= 1
            ind -= 1
        
        return