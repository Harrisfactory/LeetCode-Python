class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        cleaned_str_s = self.reverseStr(s)
        cleaned_str_t = self.reverseStr(t)
                    
        if cleaned_str_s == cleaned_str_t:
            return True
        else:
            return False
    
    
    #moves backwards ignoring backspace characters
    def reverseStr(self, s) -> str:
        
        cleaned_str = ''
        ignore_count = 0
        
        for char in reversed(s):
            if char == '#':
                ignore_count += 1
            elif char != '#' and ignore_count == 0:
                cleaned_str += char
            else:
                if ignore_count > 0:
                    ignore_count -= 1
        
        return cleaned_str