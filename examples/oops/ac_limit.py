
class Account:
      def __init__(self, id, name, balance, limit = 1000):
      #limit set to 1000 by default
            if balance < limit:
                  raise ValueError('Balance should be >= {0}'.format(limit))
            
            self.__id = id
            self.__name = name
            self.__balance = balance
            self.__limit = limit

      def __str__(self):
            return '[__id: {0}, __name: {1}, __balance: {2}, limit: {3}]'\
                   .format(self.__id, self.__name, self.__balance, self.__limit)

      def withdraw(self, amount):
            if self.__balance - amount < self.__limit:
                  raise ValueError('Minimum balance = {0} should be maintained.'.format(self.__limit))
            
            self.__balance -= amount

      def deposit(self, amount):
            self.__balance += amount

      def balance():
            return self.__balance

if __name__ == '__main__':
      ac = Account(100, 'John Doe', 1000)
      print '> initial state of a/c: ', str(ac)

      ac.withdraw(50)
      print '> state of a/c after withdrawing: ', str(ac)

      ac.deposit(150)
      print '> state of a/c after depositing: ', str(ac)
      
