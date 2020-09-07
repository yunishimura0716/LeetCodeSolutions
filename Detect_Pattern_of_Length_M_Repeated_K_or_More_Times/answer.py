class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr) < m * k:
            return False
        
        def checkSamePttn(pttn, sub):
            return all(pttn[i] == sub[i] for i in range(len(pttn)))
        
        
        ## O(n^2)
        last_idx = len(arr) - (m * k)
        for i in range(last_idx + 1):
            pattern = arr[i:i+m]
            next_i = i + m
            cnt = 1
            while next_i + m <= len(arr):
                sub = arr[next_i:next_i + m]
                print(sub)
                if checkSamePttn(pattern, sub):
                    cnt += 1
                    if cnt >= k:
                        return True
                else:
                    break
                next_i = next_i + m
        return False
