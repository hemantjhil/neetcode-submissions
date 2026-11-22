class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in countMap:
                return [countMap[diff],i]
            countMap[num]=i
        
        