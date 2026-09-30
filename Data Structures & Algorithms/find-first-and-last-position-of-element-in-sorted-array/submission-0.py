class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(target):
            lo,hi=0,len(nums)
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]<target:
                    lo=mid+1
                else:
                    hi=mid
            return lo # return the first occ where nums[i]>=target
        
        first=search(target)
        second=search(target+1)-1

        if first<=second:
            return [first,second]
        return [-1,-1]
        