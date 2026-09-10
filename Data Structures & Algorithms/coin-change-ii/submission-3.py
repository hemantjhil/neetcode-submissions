class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a][i] represents the number of combination that can create amount i using combination from amount i
        dp=[[0]*(len(coins)+1) for i in range(amount+1)]
        # base case there is exactly one way to create is to use no coins for amount 0
        dp[0]=[1]*(len(coins)+1)
        # iterate to get combination of coins for each amount
        for a in range(1,amount+1):
            # process coins from right to left
            for i in range(len(coins)-1,-1,-1):
                # Option 1 skip the current coin and use later coins
                dp[a][i]=dp[a][i+1]
                # option 2 use the current coin if it does not exceed 
                # current amount keep resuing it 
                if a-coins[i]>=0:
                    dp[a][i]+=dp[a-coins[i]][i]
        # return the combination that used to create amount
        return dp[amount][0]
        