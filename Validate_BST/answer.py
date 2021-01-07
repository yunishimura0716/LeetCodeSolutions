# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # print(2**31 -1)
        def helper(root, min_num, max_num):
            if not root:
                return True
            if min_num < root.val and root.val < max_num:
                return helper(root.left, min_num, root.val) and helper(root.right, root.val, max_num)
            else:
                return False
        return helper(root, -2**31-1, 2**31)
