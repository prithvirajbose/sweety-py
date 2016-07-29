
import unittest
import sys
sys.path.insert(0, 'C:/Courses/Tech/py/code/src')

from examples.oops.point import Point


class TestPoint(unittest.TestCase):

      def test_init(self):
            # testing origin
            self.assertEquals(str(Point()), '[x:0, y:0]')

      def test_init_other(self):
            # testing other points
            self.assertEquals(str(Point(2, 3)), '[x:2, y:3]')

      def test_set_location(self):
            p = Point()
            p.set_location(Point(2, 3))
            self.assertEquals(str(p), '[x:2, y:3]')

      def test_get_location(self):
            p = Point()
            self.assertEquals(str(p.get_location()), '[x:0, y:0]')

      def test_transpose(self):
            p = Point()
            p.transpose(-1, -1)
            self.assertEquals(str(p), '[x:-1, y:-1]')

      def test_str(self):
            p = Point()
            self.assertEquals(str(p), p.__str__())

if __name__ == '__main__':
      unittest.main(verbosity = 2)
