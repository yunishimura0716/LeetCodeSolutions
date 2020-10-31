class Solution:
    def reorderSpaces(self, text: str) -> str:
        # T(n) = O(n)
        n_space = text.count(' ')
        words = text.split()
        # print(words)
        output = ""
        if len(words) > 1:
            spaces = " " * (n_space // (len(words)-1))
            extra = " " * (n_space % (len(words)-1))
            for w in words[:-1]:
                output += "{}{}".format(w, spaces)
        else:
            extra = " " * n_space
        output += "{}{}".format(words[-1], extra)
        return output
