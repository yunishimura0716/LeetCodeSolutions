class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        return [a+extraCandies - max_num >= 0 for a in candies]
