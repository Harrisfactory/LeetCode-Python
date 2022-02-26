class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        #I want to get the initial largest amount
        largest_amount = 0
        
        kids_with_greatest = []
        
        is_greater = False
        
        for i in range(0, len(candies)):
            if largest_amount < candies[i]:
                largest_amount = candies[i]
        
        #now we go through this again and append any that match the largest amount with extra candies
        for i in range(0, len(candies)):
            if (candies[i]+extraCandies) >= largest_amount:
                is_greater = True
            else:
                is_greater = False
            kids_with_greatest.append(is_greater)
        return kids_with_greatest