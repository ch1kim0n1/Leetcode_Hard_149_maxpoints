from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        
        res = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            same = 1
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                
                slopes[(dx, dy)] += 1
            
            res = max(res, same)
            for v in slopes.values():
                res = max(res, v + same)
        
        return res
