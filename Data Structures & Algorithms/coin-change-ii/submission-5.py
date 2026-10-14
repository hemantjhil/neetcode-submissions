class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}
        def dfs(i,a):
            if a==amount:
                return 1
            if a>amount:
                return 0
            if i==len(coins):
                return 0
            if (i,a) in cache:
                return cache[(i,a)]
            cache[(i,a)]=dfs(i+1,a)+dfs(i,a+coins[i])
            return cache[(i,a)]
        return dfs(0,0)



        # # dp[a] represent number of combination to reach amount a
        # dp=[0]*(amount+1)
        # # base condition of amount 0 use no coins
        # dp[0]=1
        # # iterate through each coin so that diff ordering of same coins can be counted 1
        # for coin in coins:
        #     # calculate number of ways to form each amount using coin a 
        #     for a in range(coin,amount+1):
        #         # add number of ways to form remaining amount after using current coin
        #         dp[a]+=dp[a-coin]
        # return dp[amount]