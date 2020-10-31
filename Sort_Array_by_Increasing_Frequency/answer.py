class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # T(n) = O(nlog(n))
        elem_freq = {}
        for n in nums:
            if n in elem_freq:
                elem_freq[n] += 1
            else:
                elem_freq[n] = 1
        nums_with_freq = list(elem_freq.items())
        # print(nums_with_freq)
        nums_with_freq.sort(key=lambda x: (x[1], -x[0]))
        # print(nums_with_freq)
        
        output = []
        for nwf in nums_with_freq:
            for _ in range(nwf[1]):
                output.append(nwf[0])
        return output
