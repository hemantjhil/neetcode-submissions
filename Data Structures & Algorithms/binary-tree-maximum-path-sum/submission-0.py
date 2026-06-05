# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            leftSum=dfs(root.left)
            rightSum=dfs(root.right)
            maxLeft=max(leftSum,0)
            rightMax=max(rightSum,0)

            # max sum with split
            res[0]=max(res[0],root.val+maxLeft+rightMax)
            
            # max sum without split
            return root.val+max(maxLeft,rightMax)
        dfs(root)
        return res[0]
        