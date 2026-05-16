class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        i=0
        res,subset=[],[]

        def dfs(i,subset,total):
            if i >= len(nums) or total>target:  # Need this check
                return
            if total==target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i,subset,total+nums[i])

            subset.pop()
            dfs(i+1,subset,total)
        dfs(0,[],0)

        return res
        