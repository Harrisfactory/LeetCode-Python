class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter_bank_s = self.build_letter_bank(s)
        letter_bank_t = self.build_letter_bank(t)
                
        if letter_bank_s == letter_bank_t:
            return True
        else:
            return False
        
        
    #breaks down words into dictionaries containing letters as keys and counts of letters as values
    def build_letter_bank(self, word: str) -> dict:
        
        letter_bank = {}
        
        for letter in word:
            if letter in letter_bank:
                letter_bank[letter] += 1
            else:
                letter_bank[letter] = 1
                
        return letter_bank