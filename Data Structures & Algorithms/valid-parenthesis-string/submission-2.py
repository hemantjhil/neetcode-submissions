class Solution:
    def checkValidString(self, s: str) -> bool:
        high,low=0,0 # high max open parenthesis , low min open parenthesis
        for char in s:
            if char=='(':
                high+=1
                low+=1
            elif char==')':
                high-=1
                low-=1
            else:
                high+=1
                low-=1
            # high=3 low=1
            if high<0:
                return False
            low=max(low,0)
        return low==0
        

        