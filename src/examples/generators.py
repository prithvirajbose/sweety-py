def process_orders(orders):
      for i in orders:
            i += '_processed'
            yield i

if __name__ == '__main__':
      print type(process_orders)
      orders = ['order1', 'order2', 'order3']

      # generator function
      g = process_orders(orders)
      print type(g)

      for i in process_orders(orders):
            print i

      # generator statements
      g = (x**2 for x in range(1, 11))
      print type(g)

      for i in g:
            print i
