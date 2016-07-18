
x = int(input('Enter any integer:'))

if x < 0:
      print "Negative number..."
elif x == 0:
      print 'Zero...'
else:
      print "Positive number..."

x = int(input('Enter any integer:'))

# can be written with brackets () as well
if (x < 0):
      print "Negative number..."
      if x % 2 == 0:
            print 'By the way, It\'s divisible by 2!'
      else:
            # note the escape char '\'
            print 'By the way, it\'s an odd one!'
else:
      print 'I like your positive attitute!'



      

