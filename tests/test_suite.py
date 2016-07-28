from unittest import defaultTestLoader 
from unittest import TextTestRunner

if __name__ == '__main__':
      
      suite = defaultTestLoader\
              .loadTestsFromNames(\
                    ['sample_test.SampleTest'])

      # returns TestResult instance
      TextTestRunner(verbosity=2).run(suite)


