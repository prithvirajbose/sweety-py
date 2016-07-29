
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

#assignment solution
def myfilter(function, data):
      res = []
      for i in data:
            if function(i):
                  res.append(i)

      return res

#assignment solution
def myreduce(function, data):
      res = 1
      for i in data[1:]:
            res = function(res, i)

      return res

def square(n):
      return n ** 2
            
if __name__ == '__main__':
      
      print operation(add, 2, 3)
      print operation(multiply, 2, 3)

      print mymap(square, range(1, 5))

      #test for myfilter
      print myfilter(lambda x: x % 2 == 0, range(1, 11))
      #test for myreduce
      print myreduce(lambda acc, x: acc + x, range(1, 5))

