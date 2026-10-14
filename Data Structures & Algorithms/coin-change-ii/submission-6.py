class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] represent number of combination to reach i amount
        dp=[0]*(amount+1)
        # 1 way to reach amount 0 i.e. take no coins
        dp[0]=1
        #iterate through each coin 
        for coin in coins:
            # calculate number of ways to form each amount using coin a
            for a in range(coin,amount+1):
                # add number of ways to form remaining amount after using current coin
                dp[a]+=dp[a-coin]
        return dp[amount]
        