# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recur(node, num):
            if node==None:
                return 0
            new = num*10 + node.val
            if node.left ==None and node.right==None:
                return new
            return recur(node.left, new) + recur(node.right, new)
        return recur(root, 0)
        