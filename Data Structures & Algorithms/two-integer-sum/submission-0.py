class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap={}
        res=[]
        for i,num in enumerate(nums):
            targetDiff=target-num
            if targetDiff in sumMap:
                return [sumMap[targetDiff],i]
            sumMap[num]=i

        