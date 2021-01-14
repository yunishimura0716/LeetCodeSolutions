class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            if i <= max_idx and max_idx < i + num:
                max_idx = i + num
        # print(max_idx)
        return max_idx >= len(nums) -1
