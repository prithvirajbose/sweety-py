
import os

if __name__ == '__main__':

      input = 'README.md'
      
      # reading a text file
      with open(input) as fi:
            for line in fi:
                  print line

            # this is how you write code multiline
            print '> size of file(s): ', \
                  os.stat(input).st_size, 'bytes'
