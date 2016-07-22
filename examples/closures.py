def create_power_of(n):
      def power(x):
            return x**n
      return power

def mod(n):
      def dividend(a):
            return a % n
      return dividend

if __name__ == '__main__':
      square = create_power_of(2)
      print square(5)

      cube = create_power_of(3)
      print cube(5)

      mod2 = mod(2)
      print mod2(5)

      print mod(3)(5)
