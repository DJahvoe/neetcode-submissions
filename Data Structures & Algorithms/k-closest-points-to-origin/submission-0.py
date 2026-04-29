class Solution:
    def calculateDistance(self, x, y):
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        d_to_p = {}
        for x, y in points:
            temp_d = self.calculateDistance(x, y)
            if temp_d not in d_to_p:
                d_to_p[temp_d] = []
            d_to_p[temp_d].append([x, y])
            heapq.heappush(distance, temp_d)

        res = []
        for i in range(k):
            val = heapq.heappop(distance)
            res.append(d_to_p[val].pop())
        return res
