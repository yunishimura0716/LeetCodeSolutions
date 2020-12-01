class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [left_idx, right_idx]
        pair = [0, len(height)-1]
        max_container = 0
        while pair[0] < pair[1]:
            max_container = max(max_container, (pair[1] - pair[0]) * min(height[pair[0]], height[pair[1]]))
            if height[pair[0]] < height[pair[1]]:
                pair[0] += 1
            else:
                pair[1] -= 1
        return max_container
