from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 1
        while pivot < len(nums) and nums[pivot - 1] <= nums[pivot]:
            pivot += 1
            
        def BinSearch(a, x):
           i = bisect_left(a, x)
           if i != len(a) and a[i] == x:
              return i
           else:
              return -1
        idx1, idx2 = BinSearch(nums[:pivot], target), BinSearch(nums[pivot:], target)
        if idx2 != -1:
            idx2 += pivot
        return max(idx1, idx2)
