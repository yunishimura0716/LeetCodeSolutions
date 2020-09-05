# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        val_list = [0] * 9 ## val_list[i]: the number of node whose value is i
        odd_num = 0
        
        self.pseudoPP_check(root, val_list, odd_num, 0)
        
        return self.cnt
    
    def pseudoPP_check(self, root, val_list, odd_num, layer):
        layer += 1
        val_list[root.val - 1] += 1
        if val_list[root.val - 1] % 2 == 1:
            odd_num += 1
        else:
            odd_num -= 1
            
        if root.left == None and root.right == None:
            if self.check_pseudo(odd_num, layer):
                self.cnt += 1
        else:
            val_list_cpy = val_list.copy()
            if root.left != None:
                self.pseudoPP_check(root.left, val_list, odd_num, layer)
            if root.right != None:
                self.pseudoPP_check(root.right, val_list_cpy, odd_num, layer)

    def check_pseudo(self, odd_num, layer):
        if layer % 2 == 0:
            return odd_num == 0
        else:
            return odd_num == 1
