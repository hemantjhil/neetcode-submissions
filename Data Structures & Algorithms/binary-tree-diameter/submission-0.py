# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(node):
            nonlocal res # access the outer variable to update diameter
            if not node:
                return 0
            left=dfs(node.left) 
            right=dfs(node.right)
            res=max(res,left+right) # add height from left and right and take max
            return 1+max(left,right) #return max height
        dfs(root)
        return res
        