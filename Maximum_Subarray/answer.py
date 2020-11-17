class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) solution
        max_num = nums[0]
        max_end = nums[0]
        for i in range(1, len(nums)):
            max_end = max(max_end + nums[i], nums[i])
            max_num = max(max_num, max_end)
        return max_num
