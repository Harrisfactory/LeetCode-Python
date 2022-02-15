class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #create a dictionary to store repeating nums
        orginized_nums = {}
        
        for number in nums:
            if number not in orginized_nums:
                orginized_nums[number] = 1
            else:
                orginized_nums[number] += 1
        
        #we know there is only ONE original so
        for key in orginized_nums:
            if orginized_nums[key] == 1:
                return key