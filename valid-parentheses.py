class Solution:

    
    def isValid(self, s: str) -> bool:
    
        open_brackets = {'(': 1,'{': 2,'[': 3}
        
        closed_brackets = {')': 1,'}': 2,']': 3}
        
        if len(s) < 2 or s[0] in closed_brackets:
            return False

        counter = 0
        
        bracket_stack = []
        
        while counter < len(s):
            if s[counter] in open_brackets:
                bracket_stack.append(open_brackets.get(s[counter]))
            else:
                if len(bracket_stack) > 0:
                    if bracket_stack.pop() != closed_brackets.get(s[counter]):
                        return False
                else:
                    return False
            
            counter += 1
        
        if len(bracket_stack) > 0:
            return False
            
        return True