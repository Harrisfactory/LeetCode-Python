class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #this solution has a time complexity of O(n^2)
        
        good_pairs = 0
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                
                if nums[i] == nums[j]:
                    print("nums i equals: " + str(nums[i]) + " nums j equals: " + str(nums[j]))
                    good_pairs += 1
                    
        return good_pairs