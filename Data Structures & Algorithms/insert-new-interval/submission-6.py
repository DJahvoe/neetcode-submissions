class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            s1, e1 = intervals[i]
            s2, e2 = newInterval
            if e2 < s1:
                res.append(newInterval)
                return res + intervals[i:]
            elif s2 > e1:
                res.append(intervals[i])
            else:
                newInterval = [min(s1, s2), max(e1, e2)]
        res.append(newInterval)
        return res
