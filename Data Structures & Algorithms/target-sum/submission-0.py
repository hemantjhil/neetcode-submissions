class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Dictionary :sum count of way to reach target
        dp={0:1}
        # Process each nums
        for num in nums:
            # create new dict, can't modify existing one
            dynDP={}
            # for each sum we could make before
            for currSum,count in dp.items():
                # Option 1: Add curr num (+num)
                dynDP[currSum+num]=dynDP.get(currSum+num,0)+count
                # Option 2: Subtract curr num (-num)
                dynDP[currSum-num]=dynDP.get(currSum-num,0)+count
            # Update DP for next iteration
            dp=dynDP
        #Return count of way to reach target
        return dp.get(target,0)

        