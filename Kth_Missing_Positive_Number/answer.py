class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        next_min = 1
        for num in arr:
            if num - next_min >= k:
                return next_min + k - 1
            k -= num - next_min
            next_min = num + 1
        return next_min + k - 1
