class Solution:
    def minimumSum(self, num: int) -> int:
        
        new1 = ''
        new2 = ''
        
        num = str(num)
        num = list(num)
        
        #sort to find minimum number
        sorted_num = sorted(num)
        
        #can probably simplify this with a simple loop
        if sorted_num[0] != 0:
            new1 += sorted_num[0]
        if sorted_num[2] != 0:
            new1 += sorted_num[2]
        if sorted_num[1] != 0:
            new2 += sorted_num[1]
        if sorted_num[3] != 0:
            new2 += sorted_num[3]
        
        return int(new1) + int(new2)