class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
#         if len(arr) == 0:
#             return []
#         # O(n*log(n)) and O(n)
#         arr_cpy = arr.copy()
        
#         arr_cpy.sort()
#         rank = 1
#         rank_dict = {arr_cpy[0]:rank}
#         for i in range(1, len(arr_cpy)):
#             if not (arr_cpy[i] in rank_dict):
#                 rank += 1
#                 rank_dict[arr_cpy[i]] = rank

#         return [rank_dict[a] for a in arr]

        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, arr)
