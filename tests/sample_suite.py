import unittest

if __name__ == '__main__':
      
      suite = unittest.defaultTestLoader\
              .loadTestsFromNames(\
                    ['sample_test.SampleTest'])

      # returns TestResult instance
      unittest.TextTestRunner(verbosity=2).run(suite)


