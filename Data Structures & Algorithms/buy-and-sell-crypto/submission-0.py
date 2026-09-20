class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStock=prices[0]
        maxProfit=0;
        for price in prices[1:]:
            if price-minStock>maxProfit:
                maxProfit=price-minStock
            if price<minStock:
                minStock=price
        return maxProfit
        