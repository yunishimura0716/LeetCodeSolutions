class Solution:
    def reformat(self, s: str) -> str:
        letter_queue = []
        digit_queue = []
        for c in s:
            if c.isalpha():
                letter_queue.append(c)
            else:
                digit_queue.append(c)
        
        if abs(len(letter_queue) - len(digit_queue)) > 1:
            return ""
        
        output = ""
        if len(letter_queue) > len(digit_queue):
            while len(output) < len(s):
                if len(letter_queue) > 0:
                    output = "{}{}".format(output, letter_queue.pop(0))
                if len(digit_queue) > 0:
                    output = "{}{}".format(output, digit_queue.pop(0))
        else:
            while len(output) < len(s):
                if len(digit_queue) > 0:
                    output = "{}{}".format(output, digit_queue.pop(0))
                if len(letter_queue) > 0:
                    output = "{}{}".format(output, letter_queue.pop(0))
        return output 
