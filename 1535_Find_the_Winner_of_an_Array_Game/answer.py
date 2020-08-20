class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) - 1 <= k:
            max_num = max(arr)
            return max_num
        
        win_count = 0
        max_num = arr[0]
        for i in range(1, len(arr)):
            if max_num > arr[i]:
                win_count += 1
            else:
                max_num = arr[i]
                win_count = 1
            if win_count == k:
                return max_num
        return max_num
        