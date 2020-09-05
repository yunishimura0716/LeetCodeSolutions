class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ## O(n^2)
        soldiers_with_idx = [[sum(mat[i]), i] for i in range(len(mat))]
        
        soldiers_with_idx.sort(key = lambda x: x[0])
        
        return [l[1] for l in soldiers_with_idx[:k]]
