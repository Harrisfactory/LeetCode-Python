class Solution:
    

    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        
        right = len(nums) - 1
        
        #cant use recursion because we want to keep track of index and not value
        while left <= right:
            
            mid = (left + right) // 2
            
            #if number exists return its index
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1