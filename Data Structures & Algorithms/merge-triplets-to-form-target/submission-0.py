class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        temp = [float("-inf"), float("-inf"), float("-inf")]
        for t in triplets:
            if t[0] > target[0] or\
                t[1] > target[1] or\
                t[2] > target[2]:
                continue
            
            temp = [max(temp[0], t[0]), max(temp[1], t[1]), max(temp[2], t[2])]
        return temp == target
