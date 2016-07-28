
import unittest
from sys import platform
from unittest import TestCase

def div(x, y):
      return x/y

class SampleTest(TestCase):

      @classmethod
      def setpUpClass(cls):
            pass

      @classmethod
      def tearDownClass(cls):
            pass

      def setUp(self):
            pass

      def tearDown(self):
            pass

      def test_div(self):
            self.assertEquals(div(5, 2.0), 2.5)

      def test_error(self):
            self.assertRaises(ZeroDivisionError, div, 5, 0)

      @unittest.skip('developer has gone fishing...')
      def test_skip(self):
            pass

      @unittest.skipIf(platform == 'win32', 'test not for windows platform')
      def test_skipIf(self):
            pass

if __name__ == '__main__':
      unittest.main(verbosity = 2)
