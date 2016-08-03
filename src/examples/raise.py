      
if __name__ == '__main__':

      try:
            x = 10
            
            if x <= 10:
                  # raise exception with module name, error code and msg
                  raise ValueError('value less than 10', __name__, -1)
            
      except ValueError as e:
            msg, module, code = e.args # unpacking arguments
            print 'module={1}, err_code={2}, msg={0}'.format(msg, module, code)


