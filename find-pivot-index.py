class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        
        right = sum(nums)
        
        for i in range(0, len(nums)):
            #remove left side from right
            right -= nums[i]
            #see if at pivot point
            if left == right:
                return i
            #increment left sum
            left+=nums[i]
        
        #no solution
        return - 1