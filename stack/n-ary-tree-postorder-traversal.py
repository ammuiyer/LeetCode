"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret = []
        def recur(node):
            if not node:
                return
            else:
                for c in node.children:
                    recur(c)
                    ret.append(c.val)
        recur(root)
        ret.append(root.val)
        return ret
