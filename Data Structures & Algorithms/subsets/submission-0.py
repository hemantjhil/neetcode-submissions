class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        i=0
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return 
            
            # include nums of i (left subtree)
            subset.append(nums[i])
            dfs(i+1)

            # not include nums of i (right subtree)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        