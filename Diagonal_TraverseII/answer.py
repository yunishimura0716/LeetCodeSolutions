class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        #my solution O(A), but inefficient
#         total_nums = 0
#         for r in nums:
#             total_nums += len(r)
        
#         output = []
#         rows = len(nums)
#         curr_row = 0
#         for _ in range(rows):
#             for r in range(curr_row, -1, -1):
#                 output.append(nums[r].pop(0))
#                 if len(nums[r]) == 0:
#                     nums.pop(r)
#                     curr_row -= 1
#             curr_row += 1
        
#         while len(output) < total_nums:
#             curr_rows = len(nums)
#             for r in range(curr_rows-1, -1, -1):
#                 output.append(nums[r].pop(0))
#                 if len(nums[r]) == 0:
#                     nums.pop(r)
#         return output
            
        diagonal_list = []
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                if len(diagonal_list) <= r + c:
                    diagonal_list.append([])
                diagonal_list[r + c].append(nums[r][c])
                
        return [a for diagonal in diagonal_list for a in reversed(diagonal)]
