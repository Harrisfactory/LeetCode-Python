class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        shuffled_list = []
        
        for i in range(0, len(nums)):
            if n < len(nums):
                shuffled_list.append(nums[i])
                shuffled_list.append(nums[n])
                n += 1
                print(shuffled_list)
            
        return shuffled_list