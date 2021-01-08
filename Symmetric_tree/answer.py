# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # time: O(n), space: O(n)
#         if not root:
#             return True
        
#         def helper1(root, queue):
#             queue.append(root)
#             if not root:
#                 return
#             helper1(root.left, queue)
#             helper1(root.right, queue)
#         def helper2(root, queue):
#             tmp = queue.popleft()
#             if not root or not tmp:
#                 return tmp == root
#             return root.val == tmp.val and helper2(root.right, queue) and helper2(root.left, queue)
        
#         q = deque()
#         helper1(root.left, q)
#         return helper2(root.right, q)
        # time: O(n), space: O(1)
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            if left.val == right.val:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            else:
                return False
        if not root:
            return True
        else:
            return isMirror(root.left, root.right)
