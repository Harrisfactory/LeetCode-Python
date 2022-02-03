class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #since we are repeating twice simply start off with nums then iterate once more.

        #this solution seems to have a time complexity of O(n)
        
        for i in range(0, len(nums)):
            nums.append(nums[i])
        
        return nums