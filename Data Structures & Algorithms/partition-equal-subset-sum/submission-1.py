class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2!=0):
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            dynDP=set()
            for s in dp:
                dynDP.add(nums[i]+s)
                dynDP.add(s)
            dp=dynDP
        return True if target in dp else False
        