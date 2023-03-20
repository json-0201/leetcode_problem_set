class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        """
        Returns the index of target in the given sorted list.
        If target not found, return the index assuming it exists.
        """

        for i, num in enumerate(nums):
            if num == target:
                return i

        nums.append(target)
        nums.sort()
        
        for i, num in enumerate(nums):
            if num == target:
                return i


print(Solution().searchInsert([1,3,5,6], 7))