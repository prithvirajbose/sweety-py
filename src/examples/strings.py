
str = 'Monty Python\'s Flying Circus'

print 'str.startswith(\'Monty\'):', str.startswith('Monty')
print 'str.endswith(\'circus\'):', str.endswith('circus')
print 'str.lower().endswith(\'circus\'):', str.lower().endswith('circus')

for word in str.split(' '):
      print word, len(word)
