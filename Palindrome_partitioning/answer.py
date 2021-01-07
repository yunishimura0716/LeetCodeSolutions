class Solution:
    def partition(self, s: str) -> List[List[str]]:
        org = list(s)
        # print(org)
        result = [org]
        def make_new_partition(s_list, start, end):
            copy_list = s_list.copy()
            new_str = ''.join(copy_list[start: end+1])
            copy_list[end] = new_str
            copy_list = copy_list[:start] + copy_list[end:]
            return copy_list
        
        def partition_with_start(curr_org, begin) -> List[List[str]]:
            for i in range(begin, len(curr_org)):
                start, end = i-1, i+1
                # print(i)
                while start >= 0 and end < len(curr_org) and curr_org[start] == curr_org[end]:
                    new_org = make_new_partition(curr_org, start, end)
                    # print("new partition: ", new_org)
                    result.append(new_org)
                    partition_with_start(new_org, start + 1)      
                    start, end = start-1, end+1
                start, end = i, i+1
                while start >= 0 and end < len(curr_org) and curr_org[start] == curr_org[end]:
                    new_org = make_new_partition(curr_org, start, end)
                    # print("new partition: ", new_org)
                    result.append(new_org)
                    partition_with_start(new_org, start + 1)
                    start, end = start-1, end+1
            
        partition_with_start(org, 0)
        return result
