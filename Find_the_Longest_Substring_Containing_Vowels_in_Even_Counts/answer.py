class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ## O(n^2)
#         output = -1
#         for i in range(len(s)):
#             vowel_num_dict = {"a":0, "i":0, "u":0, "e":0, "o":0}
#             max_length = 0
#             not_even_num = 0
#             j = i
#             while j < len(s):
#                 if s[j] in vowel_num_dict:
#                     vowel_num_dict[s[j]] += 1
#                     if vowel_num_dict[s[j]] % 2 == 0:
#                         not_even_num -= 1
#                     else:
#                         not_even_num += 1
#                 if not_even_num == 0:
#                     max_length = max(max_length, j - i + 1)
#                 j += 1
#             output = max(output, max_length)
            
#         return output

        # O(n)
        # "aiueo" => "00000" : vowel_pattern
        
        vowel_pattern = "00000"
        vowel_index = {"a": 0, "i": 1, "u": 2, "e": 3, "o": 4}
        record_vowel_pattern = {vowel_pattern: -1}
        output = 0
        for i in range(len(s)):
            c = s[i]
            if c in vowel_index:
                idx = vowel_index[c]
                old = vowel_pattern[idx]
                new = str((int(old) + 1) % 2)
                vowel_pattern = "{}{}{}".format(vowel_pattern[:idx], new, vowel_pattern[idx+1:])
            if vowel_pattern in record_vowel_pattern:
                output = max(output, i - record_vowel_pattern[vowel_pattern])
            else:
                record_vowel_pattern[vowel_pattern] = i
        return output
        
