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
            if node.left ==None and node.right==None:
                return num*10 + node.val
            return recur(node.left, num*10 + node.val) + recur(node.right, num*10 + node.val)
        return recur(root, 0)
        