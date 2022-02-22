class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        #initially I see a brute force solution with nested loop
        
        current_num_count = 0
        
        higher_nums = []
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    current_num_count += 1
            higher_nums.append(current_num_count)
            current_num_count = 0
        return higher_nums
    
    #this can probably be more efficient with a sorting algorithm or done recursively
    #if sorted we would also have to check for repetitive numbers