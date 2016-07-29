
#gneral iteration
list = range(1, 101)
even_count = 0
for i in list:
      if i % 2 == 0:
            even_count += 1
print 'Number of even numbers = ', even_count

# for-loop with 'else' executing
list = ['C', 'C++', 'Java', 'C#']
for i in list:
      if i == 'Haskell':
            print 'Alas, found a pure functional language...'
else:
      print 'Searched everything, didn\'t find any functional language...'
      
# for-loop with 'else' NOT executing
list = ['C', 'Haskell', 'C++', 'Java', 'C#']
for i in list:
      if i == 'Haskell':
            print 'Alas, found a pure functional language...'
            break
else:
      print 'Searched everything, didn\'t find any functional language...'
