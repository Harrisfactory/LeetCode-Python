class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #consider the key string and compare string lengths
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        match = []
        
        s_count = 0
        #only increment s if a match is made to keep track of order
        for i in range(0, len(t)):
            
            if s_count < len(s) and t[i] == s[s_count]:
                match.append(t[i])
                s_count+=1
        
        match = ''.join(match)
        
        if match == s:
            return True
        else:
            return False