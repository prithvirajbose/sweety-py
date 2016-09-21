
import unittest
import sys
sys.path.insert(0, 'C:/Courses/Tech/py/code/src')

from examples.oops.point import Point


class TestPoint(unittest.TestCase):

      def test_init(self):
            # testing origin
            p = Point()
            self.assertEquals(p, p.get_location())

      def test_init_other(self):
            # testing other points
            p = Point(2, 3)
            self.assertEquals(p, p.get_location())

      def test_set_location(self):
            p = Point()
            p.set_location(Point(2, 3))
            self.assertEquals(p, p.get_location())

      def test_get_location(self):
            p = Point()
            self.assertEquals(str(p.get_location()), '[x:0, y:0]')

      def test_transpose(self):
            p = Point()
            p.transpose(-1, -1)
            self.assertEquals(p, p.get_location())

      def test_str(self):
            p = Point()
            self.assertEquals(str(p), '[x:0, y:0]')

if __name__ == '__main__':
      unittest.main(verbosity = 2)
