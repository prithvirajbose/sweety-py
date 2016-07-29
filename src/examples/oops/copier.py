
class Printer(object):

      def __init__(self, **kwargs):
            pass

class Scanner(object):
      def __init__(self, **kwargs):
            pass

class Copier(Printer, Scanner):

      def __init__(self, **kwargs):
            super(Copier, self).__init__(**kwargs)

if __name__ == '__main__':
      print Copier.__mro__ # method resolution order



