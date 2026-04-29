class Solution:
    def countIntervalLength(self, start, end):
        return end - start + 1

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            smallest = float("inf")
            for i in intervals:
                if i[0] <= q <= i[1]:
                    smallest = min(smallest, self.countIntervalLength(i[0], i[1]))
            if smallest == float("inf"):
                smallest = -1
            res.append(smallest)

        return res