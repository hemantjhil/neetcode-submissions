class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i,j=0,0
        maxSum=nums[0]
        sum=0
        while(i<len(nums)):
            sum+=nums[i]
            maxSum=max(sum,maxSum)
            if(sum<0):
                sum=0
            i+=1
        return maxSum
        
        