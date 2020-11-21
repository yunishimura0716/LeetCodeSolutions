class Solution:
    def romanToInt(self, s: str) -> int:
        ## make dictonary for symbot to value, T(n) = O(n)
        symbol_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if (len(s) == 1):
            return symbol_val[s]
        curr_idx = 0
        next_idx = 1
        output = 0
        while curr_idx < len(s):
            if s[curr_idx] == 'I':
                if next_idx < len(s) and (s[next_idx] == 'V' or s[next_idx] == 'X'):
                    output += symbol_val[s[next_idx]] - symbol_val[s[curr_idx]]
                    curr_idx = next_idx + 1
                    next_idx = curr_idx + 1
                    continue
            if s[curr_idx] == 'X':
                if next_idx < len(s) and (s[next_idx] == 'L' or s[next_idx] == 'C'):
                    output += symbol_val[s[next_idx]] - symbol_val[s[curr_idx]]
                    curr_idx = next_idx + 1
                    next_idx = curr_idx + 1
                    continue
            if s[curr_idx] == 'C':
                if next_idx < len(s) and (s[next_idx] == 'D' or s[next_idx] == 'M'):
                    output += symbol_val[s[next_idx]] - symbol_val[s[curr_idx]]
                    curr_idx = next_idx + 1
                    next_idx = curr_idx + 1
                    continue
            output += symbol_val[s[curr_idx]]
            curr_idx += 1
            next_idx += 1
        return output
                
