class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n_row = len(rowSum)
        n_col = len(colSum)
        A = [[-1 for _ in range(n_col)] for _ in range(n_row)]
        
        for i in range(n_row):
            for j in range(n_col):
                # print("row: {}, col: {}".format(rowSum[i], colSum[j]))
                min_num = min(rowSum[i], colSum[j])
                A[i][j] = min_num
                # print("A[{}][{}] = {}".format(i, j, min_num))
                rowSum[i] -= min_num
                colSum[j] -= min_num
        
        return A
