class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 1
        curr_length = 1
        pre_c = s[0]
        for i in range(1, len(s)):
            curr_c = s[i]
            if pre_c == curr_c:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 1
            pre_c = s[i]
        return max_length
