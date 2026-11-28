class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=i=0
        j=1
        while j<len(prices):
            if prices[j]>prices[i]:
                maxP=max(maxP,prices[j]-prices[i])
            else:
                i=j
            j+=1
        return maxP
        