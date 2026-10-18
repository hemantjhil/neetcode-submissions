class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum=max(nums)
        currMax,currMin=1,1
        for num in nums:
            if num==0:
                currMax,currMin=1,1
                continue
            tmp=num*currMax
            currMax=max(num*currMax,num*currMin,num)
            currMin=min(tmp,num*currMin,num)
            maxNum=max(currMax,maxNum)
        return maxNum
            
        