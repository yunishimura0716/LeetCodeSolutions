from functools import cache
class Solution:
    @cache
    def sumOfDigits(self, i):
        output = 0
        while i != 0:
            output += (i % 10)**2
            i //= 10
        return output
    
    def isHappy(self, n: int) -> bool:
        sets = set()
        
        while n != 1:
            n = self.sumOfDigits(n)
            # print(n)
            if n in sets:
                return False
            else:
               sets.add(n)
        return True
