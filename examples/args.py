
def with_args_kwargs(a, *args, **kwargs):
      print a, args, kwargs


def prettyprint(str, prefix = '**** ', suffix = ' ****'):
      print prefix + str + suffix

def with_args(*args):
      print type(args)
      for i in args:
            print 'type: ', type(i), ' arg=', i

def with_kwargs(**kwargs):
      print type(kwargs)
      for k, v in kwargs.iteritems():
            print 'key={0}, value={1}'.format(k, v)
      

if __name__ == '__main__':

      prettyprint('Hi')
      prettyprint('Hi', prefix = '----')
      prettyprint('Hi', suffix = '==')
      prettyprint('Hi', prefix = '/*', suffix = '*/')

      with_args(10)
      with_args(10, 'Hi there!')

      with_kwargs(name='Monty', surname='Python')
      with_kwargs(host='test.com', port =2121, protocol='rest')
      
      with_args_kwargs(100)
      with_args_kwargs(100, 'something new...')
      with_args_kwargs(100, 'something new...', n1=2)
