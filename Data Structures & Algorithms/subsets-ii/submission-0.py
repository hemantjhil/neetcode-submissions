class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(i,subset):
            if i==len(nums):
                res.append(subset[::]) # add just the copy 
                return
            
            # include the nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            # dont include nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1 #skip in case consecutive element are same
            backtrack(i+1,subset)
        backtrack(0,[])
        return res
        