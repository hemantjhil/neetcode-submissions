class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxCount=0
        for num in nums:
            if num-1 not in numSet:
                curr,count=num,0;
                while(curr in numSet):
                    curr+=1
                    count+=1
                maxCount=max(count,maxCount)
        return maxCount
        