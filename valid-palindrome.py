class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        
        right = len(s) - 1
        
        while left != right and left < len(s):
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].upper() != s[right].upper():
                        return False
                    else:
                        left += 1
                        right -= 1
                        
                else:
                    right -= 1
            else:
                left += 1
                
        return True


        #time complexity should be O(n) because each element is visited at least once