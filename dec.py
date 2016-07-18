
def imperative(list):
      sum = 0

      for i in list:
            sum += i

      return sum

def declarative(list):
      return reduce(lambda element, running_count: element + running_count, list)

if __name__ == '__main__':

      list = range(1, 11)

      print imperative(list)

      print declarative(list)
