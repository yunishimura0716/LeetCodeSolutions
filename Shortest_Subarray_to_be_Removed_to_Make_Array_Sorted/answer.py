class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        ## from front, find first increasing order: a_1, a_2, ... a_i
        first_b = len(arr)-1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                first_b = i
                break
        if first_b == len(arr) - 1:
            return 0
        
        ## from back, find last increasing order: a_j, a_j+1, ... a_n
        last_b = len(arr) - 1
        while first_b < last_b and arr[last_b-1] <= arr[last_b]:
            last_b -= 1
        print(first_b, last_b)
        output = min(len(arr) - first_b - 1, last_b)
        
        i, j = 0, last_b
        while i <= first_b and j < len(arr):
            if arr[i] <= arr[j]:
                output = min(output, j - i - 1)
                i += 1
            else:
                j += 1
        return output
        
        
