class Solution:
    def longestPalindrome(self, s: str) -> str:
        def detect_pal(s: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l+1:r]
        
        result = s[0]
        for i in range(len(s)):
            crr = detect_pal(s, i, i)
            # print(crr)
            result = crr if len(crr) > len(result) else result
            crr = detect_pal(s, i, i + 1)
            # print(crr)
            result = crr if len(crr) > len(result) else result
        return result
