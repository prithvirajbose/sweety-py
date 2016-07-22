
def operation(function, operand1, operand2):
      return function(operand1, operand2)

def avg_age(data):
      """
      Finding the avg. age of students.
      """
      '''
            x = accumulated age.
            y[1] = age from the tuple.
            
            Initializer should be set to 0.
      '''
      return reduce(lambda x, y: x + y[1], t, 0)/len(t)

def mrf(t):
      """
      Applying map, reduce, filter functions together.
      """
      # give a grace if marks < 50
      t = map(lambda student: (student[0], student[1] + 10) if student[1] < 50 else student, t)
      
      # now filter students with marks < 50
      t = filter(lambda student: student[1] < 50, t)

      # find the avg score.
      return reduce(lambda total, student: total + student[1], t, 0)/len(t)

if __name__ == '__main__':
      f = lambda x, y, z: x + y + z
      print f(3, 2, 1)

      f = lambda x, y, z = 100: x + y + z
      print f(3, 2)
      
      print operation(lambda x, y: x + y, 3, 2)
      
      print '> list of squares from 1 to 10: ', map(lambda x: x**2, range(1, 11))

      print map(lambda c: c.lower(), 'This is Python'.split(' '))

      print '> list of even numbers (1 to 10): ', filter(lambda x: x % 2 != 0, range(1, 11))

      print '> len(words) < 5: ', filter(lambda word: len(word) < 5, \
                                         'This is Python'.split(' '))


      print reduce(lambda x, y: x + y, range(1, 5))
      print reduce(lambda x, y: x + y, range(1, 5), 100)

      t = [('John', 32), ('Benny', 36), ('Oscar', 41), ('Joe', 31), ('Roger', 37)]
      print avg_age(t)

      t = [('John', 32), ('Benny', 36), ('Oscar', 41), ('Joe', 31), ('Roger', 37)]
      print mrf(t)


      
      
