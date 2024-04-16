# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val, root, None)
        def recur(node, d):
            if node is None:
                return 
            if d==depth-1:
                #add stuff
                l = node.left
                r = node.right
                node.left = TreeNode(val, l, None)
                node.right = TreeNode(val, None, r)
                return
            else:
                
                recur(node.left, d+1)
                recur(node.right, d+1)

        recur(root, 1)
        return root


        