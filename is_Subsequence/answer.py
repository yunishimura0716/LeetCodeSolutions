class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        findIdx = t.find(s[0])
        output = False
        if findIdx != -1:
            next_t = t[findIdx+1:]
            output = output or self.isSubsequence(s[1:], next_t)
        return output
