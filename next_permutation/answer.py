import bisect
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_inplace(a, start, end):
            while start < end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end -= 1
        
        for i in reversed(range(len(nums) - 1)):
            pre, curr = nums[i + 1], nums[i]
            if curr < pre:
                reverse_inplace(nums, i + 1, len(nums) - 1)
                idx = bisect.bisect_right(nums[i+1:], curr)
                next_num = nums[i + 1 + idx]
                # print(idx, next_num)
                nums[i], nums[i + 1 + idx] = next_num, curr
                return
        reverse_inplace(nums, 0, len(nums) - 1)
        return
