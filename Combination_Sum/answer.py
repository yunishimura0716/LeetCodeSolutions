from functools import cache
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        pasts = []
        self.dfs(candidates, target, pasts, output)
        return output
        
    def dfs(self, nums, target, pasts, output):
        if target < 0:
            return
        if target == 0:
            output.append(pasts)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], pasts + [nums[i]], output)
