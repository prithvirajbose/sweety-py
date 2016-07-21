
if __name__ == '__main__':

      try:
            print '> 1 before inner exception is raised...'
            try:
                  print 5/0
            except ZeroDivisionError as e:
                  print e
            else:
                  print '> 2 after inner exception block...'
            finally:
                  print '> 3 the inner finally block...'
            
      except Exception as e:
            print e
      else:
            print '> 4 after outer exception block...'
      finally:
            print '> 5 the outer finally block...'
