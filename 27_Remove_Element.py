class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        counts = nums.count(val)
        for i in range(counts):
            nums.remove(val)
        return len(nums)


print(Solution().removeElement([3,2,2,3], 3))