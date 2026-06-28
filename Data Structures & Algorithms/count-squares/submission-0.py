class CountSquares:
    #need to consider points to left, right, up, and down. if you have 3 of 4, then a valid square is formed
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []


    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(y - py) != abs(x - px)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
