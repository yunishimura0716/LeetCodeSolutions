import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numOfDown = m - 1
        numOfRight = n - 1
        return int(math.factorial(numOfDown + numOfRight) / (math.factorial(numOfDown) * math.factorial(numOfRight)))
