
class Point(object):
      def __init__(self, x = 0, y = 0):
            """By default, creates the origin."""
            self.__x = x
            self.__y = y

      def __add__(self, another):
            return Point(self.__x + another.__x, \
                         self.__y + another.__y)

      def __lt__(self, another):
            """Comparison of individual elements"""
            res = []
            if self.__x < another.__x:
                  res.append(True)
            else:
                  res.append(False)

            if self.__y < another.__y:
                  res.append(True)
            else:
                  res.append(False)

            return res
            
      def __str__(self):
            return '[x: {0}, y:{1}]'.format(self.__x, self.__y)

if __name__ == '__main__':
      p1 = Point(1,2)
      p2 = Point(3,4)

      print p1 + p2 # same as p1.__add__(p2)

      print p1 < p2
      

