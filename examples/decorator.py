
import time

def time_to_execute(f):
      """
            This function returns a function that calculates
            the execution time of a function.
      """
      def wrapper(*args):
            start = time.time()
            f(*args)
            print '> time taken to execute: {0} s'.format(time.time() - start)

      return wrapper
            
def div_validator(div):
      """
            This function returns a function that provides
            safe division (avoiding division by zero).
      """
      def div_wrapper(dividend, divisor):
            if divisor != 0:
                  return div(dividend, divisor)
            else:
                  return None

      return div_wrapper

"""
      The @div_validator ensures that any call to div(...)
      is wrapped with div_validator(...) such that all calls
      to div(...) becomes calls to div_wrapper(...)
"""
@div_validator
def div(dividend, divisor):
      return dividend/divisor

@time_to_execute
def slog():
      for i in range(10000001):
            pass
      
if __name__ == '__main__':
      print div(3, 1.5)
      print div(3, 0)

      slog()
