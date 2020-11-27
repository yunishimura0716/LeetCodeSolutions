# from bisect import bisect_left
import bisect
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) == 0 or len(nums1) == 0:
            return []
        nextGN_dict = {}
        nextGN_stack = []
        for n in nums2:
            while len(nextGN_stack) != 0 and nextGN_stack[-1] < n:
                nextGN_dict[nextGN_stack[-1]] = n
                nextGN_stack.pop()
            nextGN_stack.append(n)
        
        for i in range(len(nums1)):
            if nums1[i] in nextGN_dict:
                nums1[i] = nextGN_dict[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
                
