class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0
        for i in range(len(nums)):
            # if current position is unreachable
            if i>maxReach:
                return False
            # Update farthest reachable position
            maxReach=max(maxReach,i+nums[i])
            #early exit if we already reach the end
            if maxReach>=len(nums)-1:
                return True
        return True
        