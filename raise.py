      
if __name__ == '__main__':

      try:
            x = 10
            
            if x <= 10:
                  # raise exception with module name, error code and msg
                  raise ValueError(__name__, -1, 'value less than 10')
            
      except ValueError as e:
            module, code, msg = e.args # unpacking arguments
            print 'module=', module, ', err_code=', code, ', msg=', msg


