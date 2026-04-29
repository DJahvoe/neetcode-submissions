"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()

        res = counter = 0
        first = second = 0
        while first < len(intervals):
            if starts[first] >= ends[second]:
                second += 1
                counter -= 1
            else:
                first += 1
                counter += 1
            res = max(res, counter)
        return res

        