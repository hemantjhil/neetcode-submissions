class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] represent number of combination to reach amount a
        dp=[0]*(amount+1)
        # base condition of amount 0 use no coins
        dp[0]=1
        # iterate through each coin so that diff ordering of same coins can be counted 1
        for coin in coins:
            # calculate number of ways to form each amount using coin a 
            for a in range(coin,amount+1):
                # add number of ways to form remaining amount after using current coin
                dp[a]+=dp[a-coin]
        return dp[amount]