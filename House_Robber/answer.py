class Solution:
    def rob(self, nums: List[int]) -> int:
        ## T(n) = O(2^n)
        if len(nums) == 0:
            return 0
        # if len(nums) == 1:
        #     return nums[0]
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        ## T(n) = O(n)
        max_mem = [0] * (len(nums) + 1)
        max_mem[0] = 0
        max_mem[1] = nums[0]
        for i in range(2, len(nums)+1):
            max_mem[i] = max(max_mem[i-1], max_mem[i-2] + nums[i-1])
        return max_mem[len(nums)]
