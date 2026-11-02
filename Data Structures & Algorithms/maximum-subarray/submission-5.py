class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r=0,0
        maxSum=nums[0]
        currSum=0
        while r<len(nums):
            currSum+=nums[r]
            maxSum=max(maxSum,currSum)
            if currSum<0:
                currSum=0
            r+=1
        return maxSum

        