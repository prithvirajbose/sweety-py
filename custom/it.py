
class Counter(object):
      """
      Enables the Counter to run in a for-loop.
      """
      def __init__(self, start, stop):
            """
            start: Integer for start position
            stop: Integer, runs the Counter till stop (inclusive)
            """
            self._counter = start
            self._stop = stop

      def __iter__(self):
            return self

      def next(self):
            if self._counter > self._stop:
                  raise StopIteration
            else:
                  self._counter += 1

            return self._counter - 1

if __name__ == '__main__':
      for i in Counter(1, 5):
            print i
