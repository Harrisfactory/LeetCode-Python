class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        current_max_profit = 0
        
        #time is linear so right will always be ahead of left
        left = 0
        right = 1
        
        #while we still have days to sell
        while right < len(prices):
            
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                if (prices[right] - prices[left]) > current_max_profit:
                    current_max_profit = (prices[right] - prices[left])
                right += 1
                
                
        return current_max_profit
    
    #all elements are visited atleast once so O(n)