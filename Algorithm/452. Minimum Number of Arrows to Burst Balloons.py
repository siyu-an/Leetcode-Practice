class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        prev = points[0]
        overlap = []
        for point in points:
            if point[0] <= prev[1]:
                prev[0], prev[1] = max(point[0],prev[0]), min(point[1],prev[1])
            else:
                overlap.append(prev)
                prev = point
        overlap.append(prev)
        return len(overlap)