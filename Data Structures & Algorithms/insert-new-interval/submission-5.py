class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if intervals == []:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            res.extend(intervals)
            return res
        if newInterval[0] > intervals[-1][1]:
            res.extend(intervals)
            res.append(newInterval)
            return res

        def is_overlap(s1, e1, s2, e2):
            return not(e2 < s1 or s2 > e1)

        curr_i = 0
        is_inserted = False
        while curr_i < len(intervals):

            s1, e1 = intervals[curr_i]
            s2, e2 = newInterval
            print(res)
            print(newInterval)
            if not is_inserted and e2 < s1:
                res.append(newInterval)
                is_inserted = True

            if not is_overlap(s1, e1, s2, e2):
                res.append(intervals[curr_i])
                curr_i += 1
                continue
            
            newInterval[0], newInterval[1] = min(s1, s2), max(e1, e2)
            curr_i += 1
        if not is_inserted:
            res.append(newInterval)
        return res