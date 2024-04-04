# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m = [root.val]
        def get_max(p_root):
            if p_root == None:
                return 0
            # if p_root.left == None and p_root.right == None:
            #     m[0] = max(m[0], p_root.val)
            #     return p_root.val
            # if p_root.left == None:
            #     m[0] = max(m[0], max(p_root.val, p_root.val+get_max(p_root.right)))
            #     return max(p_root.val, p_root.val+get_max(p_root.right))
            # if p_root.right == None:
            #     m[0] = max(m[0], max(p_root.val, p_root.val+get_max(p_root.left)))
            #     return max(p_root.val, p_root.val+get_max(p_root.left))
            #split, dont split, return the dont split value
            #split
            l = max(get_max(p_root.left), 0)
            r = max(get_max(p_root.right), 0)
            m[0] = max(m[0], p_root.val+l+r)
            #return unsplit value
            return max(p_root.val, p_root.val+max(l,r))
        get_max(root)
        return m[0]

            
            