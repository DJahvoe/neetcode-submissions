class Solution:
    def is_overlap(self, s1, e1, s2, e2):
        return not(s2 > e1 or s1 > e2)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        first, second = 0, 1
        while second < len(intervals):
            s1, e1 = intervals[first]
            s2, e2 = intervals[second]

            print(intervals)
            
            if self.is_overlap(s1, e1, s2, e2):
                intervals[first] = [min(s1, s2), max(e1, e2)]
                second += 1
                continue
            
            res.append(intervals[first])
            first = second
        res.append(intervals[first])
        return res


        