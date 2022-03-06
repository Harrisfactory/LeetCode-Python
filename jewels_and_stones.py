class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        #because we are dealing with strings we don't want to manipulate them if we don't have to
        jewel_count = 0
        
        for stone in stones:
            if stone in jewels:
                jewel_count += 1 
                
        return jewel_count