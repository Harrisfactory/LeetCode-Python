class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        #build dictionary with counts from s
        orginized_letters = {}
        
        max_palindrome = 0
        
        for char in s:
            if char in orginized_letters:
                orginized_letters[char] += 1
            else:
                orginized_letters[char] = 1
        a_char = 0
        for key, value in orginized_letters.items():
            if value % 2 == 0:
                max_palindrome += value
            else:
                max_palindrome += value - 1
                a_char = 1
        
        
        return max_palindrome + a_char