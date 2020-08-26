class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #O(n*log(n))
        count_dict = {}
        for a in arr:
            if a in count_dict:
                count_dict[a] += 1
            else:
                count_dict[a] = 1
        
        count_val_list = list(count_dict.values())
        count_val_list.sort(reverse=True)
        print(count_val_list)
        
        while k > 0:
            cnt = count_val_list.pop()
            k -= cnt
            
        return len(count_val_list) + 1 if k < 0 else len(count_val_list)
