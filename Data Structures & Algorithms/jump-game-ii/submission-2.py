class Solution:
    def jump(self, nums: List[int]) -> int:
        i=j=0
        count=0
        while j<len(nums)-1:
            maxNum=0
            for k in range(i,j+1):
                maxNum=max(maxNum,nums[k]+k)
            i=j+1
            j=maxNum
            count+=1
        return count
        