# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs ( root , curr):
            if not root:
                return False

            curr += root.val

            if not root.left and not root.right:
                return curr == targetSum

            return (dfs(root.left , curr) or dfs(root.right , curr))

        return dfs(root , 0)

        # O(N) Time 
        # O(N) Space