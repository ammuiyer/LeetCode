# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if node is None:
                return
            if (node.val<=p.val and node.val>=q.val) or (node.val>=p.val and node.val<=q.val):
                return node
            else:
                if node.val>=p.val and node.val>=q.val:
                    return recur(node.left)
                else:
                    return recur(node.right)
            
        return recur(root)
        
        