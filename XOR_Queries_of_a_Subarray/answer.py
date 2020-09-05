from functools import lru_cache

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        records = [arr[0]] ## records[i] = arr[0] ^ arr[1] ^...^ arr[i]
        
        for i in range(1, len(arr)):
            records.append(records[i-1] ^ arr[i])
        
            
        return [records[r] if l == 0 else records[l - 1] ^ records[r] for l, r in queries]
