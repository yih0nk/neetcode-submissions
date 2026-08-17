from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        #num -> freq

        for num in nums:
            freq[num] += 1
        
        pairs = []
        for n in freq:
            pairs.append((freq[n], n)) #freq, num
        
        pairs.sort()
        result = []

        for i in range(len(pairs)-1, len(pairs)-k-1, -1):
            result.append(pairs[i][1])
        
        return result
                


        

