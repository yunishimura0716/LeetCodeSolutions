class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ##O(n)
        def binaryString(i: int, k: int):
            if 2**(i-1) == k:
                if i == 1:
                    return "0"
                else:
                    return "1"
            elif k < 2**(i - 1):
                return binaryString(i-1, k)
            else:## 2**(i - 1) < k
                k -= 2**(i - 1)
                output = binaryString(i-1, 2**(i-1) - k)
                return invert(output)
                
        
        def invert(c:str):
            c_inverted = "0" if int(c) % 2 == 1 else "1"
            return c_inverted
        
        return binaryString(n, k)
