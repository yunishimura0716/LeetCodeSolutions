class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        output = ""
        status = True
        idx = 0
        while status:
            if idx >= len(strs[0]):
                status = False
                continue
            c = strs[0][idx]
            for s in strs:
                if idx >= len(s) or s[idx] != c:
                    status = False
                    break
            if status:
                output += c
            idx += 1
        return output
