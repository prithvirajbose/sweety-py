
class Shape(object):
      """
      Defines the shape abstraction
      """
      def area():
            pass

      def perimeter():
            pass

class Rect(Shape):
      def __init__(self, l, b):
            self._l = l
            self._b = b

      def area(self):
            return self._l * self._b

      def perimeter(self):
            return 2 * (self._l + self._b)

class Square(Rect):
      def __init__(self, s):
            super(Square, self).__init__(s, s)
      
class Cuboid(Rect):
      def __init__(self, l, b, h):
            super(Cuboid, self).__init__(l, b)
            self._h = h

      def volume(self):
            return self.area() * self._h

      def surface_area(self):
            return self.perimeter() \
                   + 2 * (self._l * self._h + self._b * self._h)

      
if __name__ == '__main__':
      r = Rect(2, 3)
      print 'Area: {0}, Perimeter: {1}'.format(r.area(), r.perimeter())

      s = Square(2)
      print 'Area: {0}, Perimeter: {1}'.format(s.area(), s.perimeter())

      c = Cuboid(2, 3, 4)
      print 'Volume: {0}, Surface area: {1}'.format(c.volume(), c.surface_area())

