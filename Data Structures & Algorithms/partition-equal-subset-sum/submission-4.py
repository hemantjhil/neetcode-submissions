class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False
        
        dp=set()
        dp.add(0)
        target=total//2
        for i in range(len(nums)-1,-1,-1):
            dynDP=set()
            for s in dp:
                if(s+nums[i]==target):
                    return True
            
                dynDP.add(s+nums[i])
                dynDP.add(s)
            dp=dynDP
        return False