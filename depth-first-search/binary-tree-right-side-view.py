# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def rec(node, level):
            if not node:
                return
            if len(ret) > level:
                ret[level]=node.val
            else:
                ret.append(node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)
        rec(root, 0)
        
        return ret