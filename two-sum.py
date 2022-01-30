class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #brute force attempt
        
        combined_indicies = []
       
        for num in range(0, len(nums)):
            for num_next in range(num + 1, len(nums)):
                if nums[num] + nums[num_next] == target:
                    combined_indicies.append(num)
                    combined_indicies.append(num_next)
                    return combined_indicies