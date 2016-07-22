

def sort_key(person):
      return person[1]

if __name__ == '__main__':
      # a list of tuples having name and age.
      l = [('John', 32), ('Benny', 36), ('Oscar', 41), ('Joe', 31), ('Roger', 37)]

      l.sort()
      print '> sorted on name: ', l

      l.sort(key = sort_key)
      print '> sorted in ascending order of age: ', l

      l.sort(key = sort_key, reverse = True)
      print '> sorted in descending order of age: ', l
