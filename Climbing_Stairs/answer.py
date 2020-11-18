class Solution:
    def climbStairs(self, n: int) -> int:
        ## save steps # T(n) = O(n)
        steps_dict = {}
        steps_dict[1] = 1
        steps_dict[2] = 2
        for i in range(3, n+1):
            steps_dict[i] = steps_dict[i - 2] + steps_dict[i-1]
        
        return steps_dict[n]
