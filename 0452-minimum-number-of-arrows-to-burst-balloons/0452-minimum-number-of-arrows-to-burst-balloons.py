class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])
        currentArrow = sorted_points[0][1]
        arrows = 1
        i = 1
        for i in range(len(points)):
            if (sorted_points[i][0] <= currentArrow and currentArrow <= sorted_points[i][1]):
                continue
            arrows += 1
            currentArrow = sorted_points[i][1]
        return arrows

        