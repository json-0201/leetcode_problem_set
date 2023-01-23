from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_merged = nums1 + nums2
        nums_merged.sort()

        return nums_merged[len(nums_merged)//2] if len(nums_merged) % 2 == 1\
            else (nums_merged[(len(nums_merged)//2)-1] + nums_merged[len(nums_merged)//2]) / 2

print(Solution().findMedianSortedArrays([1,2],[3,4]))