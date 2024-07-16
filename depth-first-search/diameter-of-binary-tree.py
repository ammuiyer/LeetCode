# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        # Define a recursive function to calculate the diameter
        def diameter(node, res):
            if node==None:
                return 0
            left = diameter(node.left, res)
            right = diameter(node.right, res)
            ans[0] = max(ans[0], left + right)
            return max(left, right) + 1
        
        ans = [0]
        diameter(root, ans)
        return ans[0]
