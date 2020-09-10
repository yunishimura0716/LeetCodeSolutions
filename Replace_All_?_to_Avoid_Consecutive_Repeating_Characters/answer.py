class Solution:
    def modifyString(self, s: str) -> str:
        ## we need just three character a, b, c
        pre_c, pro_c = "" ,""
        for i in range(len(s) - 1):
            pro_c = s[i+1]
            if s[i] == "?":
                if pre_c == "a" or pro_c == "a":
                    if pre_c == "b" or pro_c == "b":
                        s = s[:i] + "c" + s[i+1:]
                    else:
                        s = s[:i] + "b" + s[i+1:]
                else:
                    s = s[:i] + "a" + s[i+1:]
            pre_c = s[i]
        
        pro_c = ""
        if s[len(s) - 1] == "?":
            if pre_c == "a" or pro_c == "a":
                if pre_c == "b" or pro_c == "b":
                    s = s[:len(s) - 1] + "c"
                else:
                    s = s[:len(s) - 1] + "b"
            else:
                s = s[:len(s) - 1] + "a"
        return s
