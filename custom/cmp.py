
"""
This is a demo on how to use the 'cmp' function.
In production use 'key' - it is faster and enables
one to write neat code.
"""
def compare(person1, person2):
      """Function takes two arguments and return -1, 1 or 0."""
      if person1.get_name() < person2.get_name():
            return -1
      elif person1.get_name() > person2.get_name():
            return 1
      else:
            return 0
      
class Person(object):
      def __init__(self, name, age):
            self._name = name
            self._age = age

      def __str__(self):
            return 'name: {0}, age: {1}'.format(self._name, self._age)

      def get_name(self):
            return self._name

if __name__ == '__main__':
      p1 = Person('Oswald', 20)
      p2 = Person('Billy', 21)
      p3 = Person('Oscar', 23)
      p4 = Person('Benny', 19)
      
      persons = [p1, p2, p3, p4]

      persons.sort(cmp = compare)
      #names.sort(key = lambda person: person.get_name())

      for person in persons:
            print person
            
