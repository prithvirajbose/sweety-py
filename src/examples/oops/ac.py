
class Account(object):
      def __init__(self, id, name, balance):
            self.id = id
            self.name = name
            self.balance = balance

      def __str__(self):
            return '[id: {0}, name: {1}, balance: {2}]'\
                   .format(self.id, self.name, self.balance)

      def withdraw(self, amount):
            self.balance -= amount
            return self.balance

      def deposit(self, amount):
            self.balance += amount
            return self.balance

if __name__ == '__main__':
      ac = Account(100, 'John Doe', 100)
      print '> initial state of a/c: ', str(ac)

      ac.withdraw(50)
      print '> state of a/c after withdrawing: ', str(ac)

      ac.deposit(150)
      print '> state of a/c after depositing: ', str(ac)

      print ac.id, ac.name, ac.balance
      
