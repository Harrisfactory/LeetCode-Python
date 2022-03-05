class Solution:
    def removeVowels(self, s: str) -> str:
        
        for char in s:
            if char in "aeiou":
                s = s.replace(char,'')
        return s