# -*- coding: cp1252 -*-

import os

if __name__ == '__main__':

      input = '..\README.md'    
      output = '..\copy_README.md'

      # copy text file      
      with open(input) as fi, open(output, 'w') as fo:
            # it’s your problem if the file is twice as large as your machine’s memory
            fo.write(fi.read())
            
      input = '..\python.png'    
      output = '..\copy_python.png'
      # copy binary file      
      with open(input, 'rb') as fi, open(output, 'wb') as fo:
            fo.write(fi.read())


