
class Car(object):

      def __init__(self, model, colour):
            self._model = model
            self._colour = colour

class Sedan(Car):

      def __init__(self, model, colour, price):
            super(Sedan, self).__init__(model, colour)
            self._price = price

      def __str__(self):
            return '[name: {0}, colour: {1}, price: {2}]'\
                   .format(self._model, self._colour, self._price)

if __name__ == '__main__':
      c = Sedan('s-cross', 'black', 800000)
      print c
      
            
