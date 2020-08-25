class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        output = evens = odds = 0
        
        for a in arr:
            if a % 2 == 0:
                evens = evens + 1
                odds = odds
            else:
                t = evens
                evens = odds
                odds = t + 1
            # print(odds)
            output += odds
        
        return output % (10**9 + 7)
