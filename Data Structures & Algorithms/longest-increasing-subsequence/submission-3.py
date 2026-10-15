class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)

        # def dfs(prev_index,index):
        #     if index==len(nums):
        #         return 0
            
        #     skip=dfs(prev_index,index+1)

        #     take=0;
        #     if prev_index==-1 or nums[prev_index]<nums[index]:
        #         take=1+dfs(index,index+1)
        #     return max(skip,take)
        # return dfs(-1,0)
        