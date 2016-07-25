
import sys
import keyword

def sys_path():
      print __name__ + '.sys_path() called'
      return sys.path

def keywords():
      print __name__ + '.keywords() called'
      return keyword.kwlist

