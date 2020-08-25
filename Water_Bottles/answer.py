class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #O(log(n))
        
#         full_buttle = numBottles
#         empty_buttle = 0
        
#         drink_num = 0
#         while full_buttle > 0:
#             drink_num += full_buttle
#             empty_buttle += full_buttle
#             full_buttle = empty_buttle // numExchange
#             empty_buttle = empty_buttle % numExchange
        
#         return drink_num

        #O(1)
        """The thing that we can exchange full water of bottle with numExchange of empty bottle
        means that we can exchange full water with (numExchange-1) of empty bottle.
        So, while remaining one bottle for drinking, we can calculate amount of full water from
        (numBottles - 1) // (numExchange - 1) """
        
        return numBottles + (numBottles - 1) // (numExchange - 1)
