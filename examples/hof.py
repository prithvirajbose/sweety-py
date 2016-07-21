
def add(a, b):
      return a + b

def multiply(a, b):
      return a * b

def operation(function, operand1, operand2):
      return function(operand1, operand2)

def mymap(function, data):
      res = []
      for i in data:
            res.append(function(i))

      return res

def square(n):
      return n ** 2
            
if __name__ == '__main__':
      
      print operation(add, 2, 3)
      print operation(multiply, 2, 3)

      print mymap(square, range(1, 5))

