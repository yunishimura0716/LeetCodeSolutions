class Solution:
    count = 0
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.getDistances(root, distance)
        
        return self.count
    
    def getDistances(self, root: TreeNode, distance):
        if root.left == None and root.right == None:
            return [1]
        if root.left == None:
            return [i+1 for i in self.getDistances(root.right, distance) if i+2 <= distance]
        if root.right == None:
            return [i+1 for i in self.getDistances(root.left, distance) if i+2 <= distance]
        
        
        leftDistances = self.getDistances(root.left, distance)
        rightDistances = self.getDistances(root.right, distance)
        
        distances = []
        
        for left_n in leftDistances:
            for right_n in rightDistances: 
                sum_num = left_n + right_n
                if sum_num <= distance:
                    self.count += 1
        
        for right_n in rightDistances:
            if right_n + 2 <= distance:
                    distances.append(right_n+1)
        for left_n in leftDistances:
            if left_n + 2 <= distance:
                distances.append(left_n+1)
        return distances
