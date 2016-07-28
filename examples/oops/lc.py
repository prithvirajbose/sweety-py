
class LifeCycle(object):
      def __init__(self):
            print '__init__ called...'

      def __del__(self):
            print '__del__ called...'

if __name__ == '__main__':
      lc = LifeCycle()
      del lc
            
