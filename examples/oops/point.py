
class Point(object):
      """
            Models Cartesian coordinates on two dimension, X-Y plane
      """

      def __init__(self, x = 0, y = 0):
            """
                  Creates a point with the x & y coordinates.
                  By default, creates the origin.
            """
            self.__x = x
            self.__y = y

 
      def getlocation(self):
            """
                  Return the location as a point.
            """
            return self

      def setlocation(self, point):
            """
                  Set the location to a new point.
            """
            self.__x = point.__x
            self.__y = point.__y

      def transpose(self, dx, dy):
            """
                  Move the point to a new location by dx, dy.
            """
            self.__x += dx
            self.__y += dy

      def __str__(self):
            """
                  Returns the string representation of the point.
            """
            return '[x: {0}, y:{1}]'.format(self.__x, self.__y)

if __name__ == '__main__':
      p = Point(1,2)
      
      print p.getlocation()

      p.setlocation(Point(3, 9))
      print p.getlocation()

      p.transpose(1, 1)
      print p.getlocation()
      print 
