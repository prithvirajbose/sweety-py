
if __name__ == '__main__':
      a = [1, 2, 3, 11, 13, 13, 15]
      print '> original list: ', a
      a.append(16)
      print '> append 16: ', a

      b = range(1, 5) # equivalent to b = [1, 2, 3, 4]
      a.extend(b)
      print '> add another list\'s contents: ', a

      a.insert(0, -1)
      print '> add -1 at 0 index: ', a
      a.remove(-1)
      print '> remove -1 from 0 index: ', a

      a.pop(1)
      print '> pop the second element: ', a

      a.pop(0)
      print '> pop the first element now: ', a
      
      print '> return the index of 11: ', a.index(11)

      print '> count the occurrences of 3 & 13: ', a.count(3), ',',  a.count(13)

      a.reverse()
      print '> reversed list: ', a

      a.sort()
      print '> sorted list (asc.): ', a 
      a.sort(reverse = True)
      print '> sorted list (desc.): ', a

      print '> prints the second last element: ', a[-2]

      # insert, update, delete ops on list
      a.insert(0, -1)
      print '> insert -1 at 0 index: ', a
      a[0] = -100
      print '> update the first element: ', a
      del a[0]
      print '> delete the first element: ', a 
