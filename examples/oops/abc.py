
from abc import ABCMeta, abstractmethod

class AbstractClass(object):
      __metaclass__ = ABCMeta

      @abstractmethod
      def some_method(self):
            pass

class ConcreteClass(AbstractClass):
      # overrides the base class method some_method()
      def some_method(self): 
            pass

if __name__ == '__main__':
      try:
            a = AbstractClass()
      except TypeError as e:
            print e

      ConcreteClass().some_method()
      
