class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sorting O(nlog(n))
        nums.sort()
        
        # find closest O(n^2)
        close_dis = 100000
        closest = 0
        for i in range(len(nums) - 2):
            left_i = i + 1
            right_i = len(nums) - 1
            curr_target = target - nums[i]
            while left_i < right_i:
                curr_sum = nums[left_i] + nums[right_i]
                if abs(curr_target - curr_sum) < close_dis:
                    close_dis = abs(curr_target - curr_sum)
                    closest = curr_sum + nums[i]
                if curr_sum > curr_target:
                    right_i -= 1
                else:
                    left_i += 1
        return closest
