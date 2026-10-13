class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1 # 1 way to reach 0 sum
        for num in nums:
            curr_dp=defaultdict(int)
            for total,count in dp.items():
                curr_dp[total+num]+=count
                curr_dp[total-num]+=count
            dp=curr_dp
        return dp[target]

        