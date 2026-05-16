class Solution:
    def isHappy(self, n: int) -> bool:
        
        def nextNum(n):
            sum=0
            while(n>0):
                digit=n%10
                sum+=digit**2
                n//=10
            return sum
        slow=n
        fast=nextNum(n)
        while(slow!=fast and fast!=0):
            slow=nextNum(slow)
            fast=nextNum(nextNum(fast))
        return slow==1

            

        