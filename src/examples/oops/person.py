
class Person(object):
      """
      A class to model a person.
      Attributes: name, age
      Methods: constructor, str
      """
      def __init__(self, name, age):
            self.name = name
            self.age = age

      def __str__(self):
            return '[name:{0}, age:{1}]'.format(self.name, self.age)


if __name__ == '__main__':
      p = Person('Prithviraj Bose', 18)
      print p # same as str(p)
      print p.name, p.age
      print dir(p)



