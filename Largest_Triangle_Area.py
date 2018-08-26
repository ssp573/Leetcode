class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area=0
        for point1 in points:
            for point2 in points:
                for point3 in points:
                    if point1!=point2 and point2!=point3 and point3!=point1:
                        area=self.triangle_area(point1,point2,point3)
                        if area>max_area:
                            max_area=area
        return max_area
                            
    def triangle_area(self, a, b, c):
		return (0.5*abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])))
