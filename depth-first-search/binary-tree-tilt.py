# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def sum(node):
            if node == None:
                return 0
            return node.val + sum(node.left) + sum(node.right)
        
        # print(sum(root.left))
        # print(sum(root.right))
        def tilt(node):
            if node == None:
                return 0 
            return abs(sum(node.left) - sum(node.right)) + tilt(node.left) + tilt(node.right)
        return (tilt(root))
        
        