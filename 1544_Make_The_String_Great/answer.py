class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        new_s = [s[0]]
        while i < len(s):
            top_i = len(new_s) - 1
            if top_i < 0:
                new_s.append(s[i])
            elif self.isAdjacent(new_s[top_i], s[i]):
                new_s.pop()
            else:
                new_s.append(s[i])
            i += 1
        return ''.join(new_s)
        
    def isAdjacent(self, c1, c2):
        if c1 != c2 and c1.lower() == c2.lower():
            return True
        else:
            return False