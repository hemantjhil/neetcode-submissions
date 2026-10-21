class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
        # s=""
        # quo=n
        # count=0
        # while quo>1:
        #     rem=n%2
        #     if rem==1:
        #         count+=1
        #     s.add(rem)
        #     quo=n//2
        #     n=quo
        # return count
        
        


        