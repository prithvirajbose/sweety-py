
from abc import ABCMeta, abstractmethod

class AbstractFile(object):

      __metaclass__ = ABCMeta
      
      _filename = None # protected member, inherited by the sub-classes.

      @abstractmethod
      def open_file(self):
            pass

      def save_file(self):
            pass

class MyFile(AbstractFile):

      def __init__(self, filename):
            self._filename = filename
            
      def open_file(self):
            print 'MyFile.open_file called'

      def save_file(self):
            print 'MyFile.save_file called'

class MyCompressedFile(MyFile):
      
      def __init__(self, filename):
            super(MyCompressedFile, self).__init__(filename)

      def open_file(self):
            print 'MyCompressedFile.open_file called'

      def save_file(self):
            #put the compression logic
            print 'MyCompressedFile.save_file called'
            super(MyCompressedFile, self).save_file()

if __name__ == '__main__':
      f = MyCompressedFile('somefile.txt')
      f.open_file()
      f.save_file()
