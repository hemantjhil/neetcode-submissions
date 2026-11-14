class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        sumNum=0
        minLength=float("inf")
        while j<len(nums):
            sumNum+=nums[j]
            while sumNum>=target:
                minLength=min(minLength,j-i+1)
                sumNum-=nums[i]
                i+=1
            j+=1
        return minLength if minLength!=float("inf") else 0
                
        
        