

def sort_key(person):
      return person[1]

def comp(person1, person2):
      if person1[1] < person2[1]:
            return -1
      elif person1[1] > person2[1]:
            return 1
      else:
            return 0

if __name__ == '__main__':
      # a list of tuples having name and age.
      l = [('John', 32), ('Benny', 36), ('Oscar', 41), ('Joe', 31), ('Roger', 37)]

      l.sort()
      print '> sorted on name: ', l

      l.sort(key = sort_key)
      print '> sorted using key: ', l

      l.sort(cmp = comp)
      print '> sorted using cmp: ', l

      l.sort(key = sort_key, reverse = True)
      print '> sorted in descending order of age: ', l
