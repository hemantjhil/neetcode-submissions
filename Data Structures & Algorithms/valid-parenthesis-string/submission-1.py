class Solution:
    def checkValidString(self, s: str) -> bool:
        
        low=0 # min open parenthesis
        high=0 # max open parenthesis
        for char in s:
            if char=='(':
                low+=1
                high+=1
            elif char==')':
                low-=1
                high-=1
            else: # for *
                low-=1 # Treat * as )
                high+=1 # Treat * as (
        
            #if high becomes negative too many )
            if high<0:
                return False
            # Low can't go below 0 (can't have neagtive open params)
            low=max(low,0)
            # Valid if we have 0 open params at the end
        return low==0
            
        