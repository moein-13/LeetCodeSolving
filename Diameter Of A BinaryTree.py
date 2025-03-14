# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0
        
        def length (root):
            if not root:
                return 0 

            left_length = length(root.left)
            right_length = length(root.right)

            self.diameter = max(self.diameter , left_length + right_length)
            return 1 + max(left_length , right_length)

        length(root)

        return self.diameter

        # Time complexity : O(n)
        # Space complexity: O(h)
