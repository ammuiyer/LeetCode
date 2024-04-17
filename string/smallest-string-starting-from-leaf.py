# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        minstr = [""]
        def recur(node, string):
            if node.left==None and node.right==None:
                #reverse string
                string+=chr(node.val+97)
                string = string[::-1]
                #print(string, minstr[0])
                # if string[0] == "b" and len(minstr[0])==len(string)-1:
                #     minstr[0] = string
                if string<minstr[0] or minstr==[""]:
                    minstr[0] = string
                return
            else:
                    if node.left:
                        recur(node.left, string+chr(node.val+97))
                    if node.right:
                        recur(node.right, string+chr(node.val+97))

        recur(root, "")
        return minstr[0]
        