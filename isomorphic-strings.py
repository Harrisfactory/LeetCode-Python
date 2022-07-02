class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dict_s = {}
        dict_t = {}
        #if the char at current index is not in respective dictionaries place them with that specific index 
        #then comare each by its index
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = i
            if t[i] not in dict_t:
                dict_t[t[i]] = i
            if dict_s[s[i]] != dict_t[t[i]]:
                return False
        return True