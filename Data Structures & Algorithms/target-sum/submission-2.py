class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp=defaultdict(int)
        dp[0]=1
        
        for num in nums:
            dynDP=defaultdict(int)
            for total,count in dp.items():
                dynDP[total+num]+=count
                dynDP[total-num]+=count
            dp=dynDP
        return dp[target]


        