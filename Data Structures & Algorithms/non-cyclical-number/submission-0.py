class Solution:
    def isHappy(self, n: int) -> bool:

        numSet=set()
        while(n!=1):
            sum=0
            while(n>0):
                digit=n%10
                sum+=digit**2
                n//=10
            if(sum in numSet):
                return False
            if(sum/10<1):
                numSet.add(sum)
            n=sum
        return True
            

        