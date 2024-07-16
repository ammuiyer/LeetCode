# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(node):
            if node==None:
                return 0, True
            else:
                l = recur(node.left)
                if l!=False:
                    l = l[0]
                else:
                    return False
                r = recur(node.right)
                if r!=False:
                    r = r[0]
                else:
                    return False
                height = max(l, r) + 1
                #print(node.val, l, r)
                if l == r or l == r-1 or l==r+1:
                    return height, True
                else:
                    return False
        return recur(root)
        