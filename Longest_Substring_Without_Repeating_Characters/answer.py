class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T(n) = O(n)
        char_dict = dict()
        longest = 0
        start_idx = 0
        for i in range(len(s)):
            c = s[i]
            if c in char_dict and start_idx <= char_dict[c]:
                start_idx = char_dict[c] + 1
            else:
                print
                longest = max(longest, i - start_idx  + 1)
            char_dict[c] = i
        return max(longest, len(s) - start_idx)  
