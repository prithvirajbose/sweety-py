
if __name__ == '__main__':

      existingFile = 'README.md'
      notExistingFile = 'someFile.txt'
      try:
            with open(notExistingFile) as f:
                  for line in f:
                        print line
      except IOError as error:
            print error
      else:
            print '> executing after exception...'
      finally:
            print '> executing the finally block...'
            
