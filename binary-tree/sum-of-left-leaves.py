# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node==None:
                return 0
            else:
                if node.left!=None and node.left.left==None and node.left.right==None:
                    return node.left.val + helper(node.left) + helper(node.right)
                return helper(node.left) + helper(node.right)
        return helper(root)
        