from fractions import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ##O(n^2*logn)
        if n == 1:
            return []
        
        output = []
        
        for denom in range(2, n+1):
            for nume in range(1, denom):
                gcd_n = gcd(nume, denom)
                if gcd_n > 1:
                    continue
                output.append("{}/{}".format(nume//gcd_n, denom//gcd_n))
        return output
