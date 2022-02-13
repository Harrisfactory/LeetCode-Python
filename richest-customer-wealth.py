class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        #returning max wealth
        max_wealth = 0
        
        current_wealth = 0
        
        for i in range(0, len(accounts)):
            for j in range(0, len(accounts[i])):
                current_wealth += accounts[i][j]
            
            if max_wealth < current_wealth:
                max_wealth = current_wealth
                current_wealth = 0
            else:
                current_wealth = 0
        return max_wealth
        