
class Account(object):
      def __init__(self, __id, __name, __balance):
            self.__id = __id
            self.__name = __name
            self.__balance = __balance

      def __str__(self):
            return '[__id: {0}, __name: {1}, __balance: {2}]'\
                   .format(self.__id, self.__name, self.__balance)

      def withdraw(self, amount):
            self.__balance -= amount
            return self.__balance

      def deposit(self, amount):
            self.__balance += amount
            return self.__balance

if __name__ == '__main__':
      ac = Account(100, 'John Doe', 100)
      print '> initial state of a/c: ', str(ac)

      ac.withdraw(50)
      print '> state of a/c after withdrawing: ', str(ac)

      ac.deposit(150)
      print '> state of a/c after depositing: ', str(ac)

      print ac._Account__name
