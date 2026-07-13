import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        #closest = math.sqrt((points[0][0] - 0)**2 + (points[0][1] - 0)** 2)
        for x,y in points:
            distance = (x**2) + (y**2)
            distances.append([distance,x,y])
        heapq.heapify(distances)
        sol = []
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            sol.append([x,y])
            k -= 1
        
        return sol



