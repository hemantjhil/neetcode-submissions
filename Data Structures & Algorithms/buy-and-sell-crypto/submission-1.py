class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=i=j=0
        while i<len(prices):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j];
                maxP=max(maxP,sell-buy)
            i+=1
        return maxP