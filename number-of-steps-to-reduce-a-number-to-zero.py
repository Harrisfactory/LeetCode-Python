class Solution:
    
    steps = 0
    
    def numberOfSteps(self, num: int) -> int:
        
        #edge case num is already 0
        if num == 0:
            return 0
    
        #is even
        if num % 2 == 0:
            num = num // 2
            self.steps += 1
        else:
            num = num - 1
            self.steps += 1
        
        if num != 0:
            self.numberOfSteps(num)
        
        return self.steps

      