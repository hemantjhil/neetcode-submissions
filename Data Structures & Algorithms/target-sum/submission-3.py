class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dict sum count of ways to reach target
        dp={0:1}
        # process each nums
        for num in nums:
            # create new dict cant modify existing one
            dynDP={}
            # for each sum we could make before
            for currSum,count in dp.items():
                # option 1: add curr num(+num)
                dynDP[currSum+num]=dynDP.get(currSum+num,0)+count
                # option 2: subtract curr num(-num)
                dynDP[currSum-num]=dynDP.get(currSum-num,0)+count
            # update DP for next iteration
            dp=dynDP
        # return count of ways to reach target
        return dp.get(target,0)

        