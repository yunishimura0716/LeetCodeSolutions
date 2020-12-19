# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        def constUnique(minn, maxnn):
            if minn > maxnn:
                return [None]
            if minn == maxnn:
                node = TreeNode(minn)
                return [node]
            
            output = []
            for i in range(minn, maxnn + 1):
                left = constUnique(minn, i - 1)
                right = constUnique(i + 1, maxnn)
                for ln in left:
                    for rn in right:
                        node = TreeNode(i, ln, rn)
                        output.append(node)
            return output
        return constUnique(1, n)
