# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        return self.searchSubPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
        
    def searchSubPath(self, head: ListNode, root):
        if head == None:
            return True
        if root == None:
            return False
        
        return head.val == root.val and (self.searchSubPath(head.next, root.left) or self.searchSubPath(head.next, root.right))
