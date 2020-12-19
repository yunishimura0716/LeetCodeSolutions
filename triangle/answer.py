class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        
        output = [[-1 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        output[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            output[i][0] = triangle[i][0] + output[i - 1][0]
        for row in range(1, len(triangle)):
            for col in range(1, len(triangle[row])):
                if col == len(triangle[row]) - 1:
                    output[row][col] = triangle[row][col] + output[row - 1][col - 1]
                else:
                    output[row][col] = triangle[row][col] + min(output[row - 1][col - 1], output[row - 1][col])
        # print(output)
        return min(output[len(triangle) - 1])
