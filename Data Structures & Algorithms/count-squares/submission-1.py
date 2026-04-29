class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        return res
        
