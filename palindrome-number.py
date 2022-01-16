class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted_x = str(x)
        
        number_length = len(converted_x)
        
        for index, item in enumerate(converted_x):
            print("front index is: " + str(index) + " and the number is: " + item)
            
            print("back index is: " + str(len(converted_x) - index) + " and the number is: " + converted_x[(len(converted_x) - 1) - index])
            
            if item != converted_x[(len(converted_x) - 1) - index]:
                return False
        return True