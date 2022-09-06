import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i, point in enumerate(points):
            e_d = point[0]*point[0] + point[1]*point[1]
            point.insert(0, e_d)
            points[i] = point
        heapq.heapify(points)
        res = []
        for i in range(k):
            res.append(heapq.heappop(points)[1:])
        return res
        