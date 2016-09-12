
if __name__ == '__main__':

      # for-loop with 'else' executing
      list = ['C', 'C++', 'Java', 'C#', 'Haskell']
      for i in list:
            if i == 'Haskell':
                  print 'Alas, found a pure functional language...'
                  break
      else:
            print 'Searched everything, didn\'t find any functional language...'
