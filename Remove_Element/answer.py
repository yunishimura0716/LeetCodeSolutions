class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        cnt = 0
        for n in nums:
            if n == val:
                cnt += 1
        
        while left_idx < right_idx:
            if nums[left_idx] == val:
                while left_idx < right_idx and nums[right_idx] == val:
                    right_idx -= 1
                t = nums[left_idx]
                nums[left_idx] = nums[right_idx]
                nums[right_idx] = t
                left_idx += 1
            else:
                left_idx += 1
        return len(nums) - cnt
