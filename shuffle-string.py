class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        shuffled = {}
        
        shuffled_string = ''
        
        cur = 0
        
        for i in range(0, len(indices)):
            shuffled[indices[i]] = s[i]
        
        while cur < len(s):
            shuffled_string += str(shuffled[cur])
            cur += 1
            
        return shuffled_string
                    