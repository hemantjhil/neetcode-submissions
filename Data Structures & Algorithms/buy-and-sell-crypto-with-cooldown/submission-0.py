class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold=-prices[0]
        sold=0
        rest=0
        for price in prices[1:]:
            prev_hold,prev_sold,prev_rest=hold,sold,rest
            hold=max(prev_hold,prev_rest-price)
            sold=price+prev_hold
            rest=max(prev_sold,prev_rest)
        return max(sold,rest)
        