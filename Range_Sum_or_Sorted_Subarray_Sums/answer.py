class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ##O(n^2 * log(n))
        sums = []
        for l in range(n):
            curr_sum = 0
            for r in range(l, n):
                curr_sum += nums[r]
                sums.append(curr_sum)
        
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)
