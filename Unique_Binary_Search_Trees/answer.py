class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        numTrees_dict = {}
        numTrees_dict[0] = 1
        numTrees_dict[1] = 1
        for i in range(2, n+1):
            numTrees_dict[i] = 0
            for left_num in range(i):
                numTrees_dict[i] += numTrees_dict[left_num]*numTrees_dict[i - left_num - 1]
        return numTrees_dict[n]
