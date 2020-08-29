class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        partner_set = set()
        
        for a in arr:
            if a in partner_set:
                return True
            if a % 2 == 0:
                partner = a // 2
                partner_set.add(partner)
            partner = a * 2
            partner_set.add(partner)
        return False
