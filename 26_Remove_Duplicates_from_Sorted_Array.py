class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # nums = creates a new list object
        # nums[:] = updates original list elements
        
        nums[:] = set(nums)
        nums.sort()
        
        return len(nums)

    
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
