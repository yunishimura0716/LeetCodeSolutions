class Solution:
    output = []
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.output = [0] * n
        node_dict = {}
        node_dict_1 = {}
        node_dict_2 = {}
        for edge in edges:
            if edge[0] in node_dict_1:
                node_dict_1[edge[0]].append(edge[1])
            else:
                node_dict_1[edge[0]] = [edge[1]]
            if edge[1] in node_dict_2:
                node_dict_2[edge[1]].append(edge[0])
            else:
                node_dict_2[edge[1]] = [edge[0]]
        # print(node_dict_1)
        # print(node_dict_2)
        node_stack = [0]
        while len(node_stack) > 0:
            node = node_stack.pop()
            if node in node_dict_1:
                node_dict[node] = []
                for child in node_dict_1[node]:
                    node_dict[node].append(child)
                    node_stack.append(child)
                    node_dict_2[child].remove(node)
                    if len(node_dict_2[child]) == 0:
                        del node_dict_2[child]
            elif node in node_dict_2:
                node_dict[node] = []
                for child in node_dict_2[node]:
                    node_dict[node].append(child)
                    node_stack.append(child)
                    node_dict_1[child].remove(node)
                    if len(node_dict_1[child]) == 0:
                        del node_dict_1[child]
            
        # print(node_dict)
        self.getLabelCount(0, node_dict, labels)
        
        return self.output
        
        
    def getLabelCount(self, node_val, node_dict, labels):
        ## count each label's count in subtree
        count_dict = {}
        if node_val not in node_dict:
            self.output[node_val] = 1
            return {labels[node_val]:1}
        
        for node in node_dict[node_val]:
            chi_count_dict = self.getLabelCount(node, node_dict, labels)
            for chi_label in chi_count_dict:
                count = chi_count_dict[chi_label]
                if chi_label in count_dict:
                    count_dict[chi_label] += count
                else:
                    count_dict[chi_label] = count
        ## get the count of this node's label
        node_label = labels[node_val]
        label_count = 0
        if node_label in count_dict:
            label_count = count_dict[node_label]
        
        ## update output and count_dict
        label_count+=1
        count_dict[node_label] = label_count
        self.output[node_val] = label_count
        
        return count_dict
