
if __name__ == '__main__':
      d = {1: 'Johnny', 2: 'Benny', 3: 'Mandy', 4: 'Oscar', 5: 'Louis'}
      print '> dict: ', d
      print '> value of key=1 :', d[1]
      d[1] = 'Sandy'
      print '> update value=\'Sandy\' for key=1 :', d[1]
      print '> value of key=20 :', d.get(20, 'Key not found')
      print '> key=2 exists? :', 2 in d

      print '> print the dict contents'
      for i in d.keys():
            print i, d[i]

      del d[5]
      print '> key=5 exists? :', 5 in d

      d.clear() #clears the dict
      print '> dict after clear(): ', d

      # dict views
      d = {1: 'Johnny', 2: 'Benny', 3: 'Mandy', 4: 'Oscar', 5: 'Louis'}
      view = d.viewitems()

      print '> contents from dict view: ', view

      del d[1]

      print '> contents from dict view after key=1 deleted: ', view
      
