class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's Algo
        # Track running sum and reset to 0 when it goes negative
        # Keep track of the maximum sum seen so far
        i=0
        maxSum=nums[0]
        sum=0
        while(i<len(nums)):
            sum+=nums[i]
            maxSum=max(sum,maxSum)
            if(sum<0):
                sum=0
            i+=1
        return maxSum
        
        