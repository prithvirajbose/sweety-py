# for-loop with 'break'
list = ['C', 'Haskell', 'C++', 'Java', 'C#']
for i in list:
      if i == 'Haskell':
            print 'Alas, found a pure functional language...'
            break
else:
      print 'Searched everything, didn\'t find any functional language...'


# for-loop with 'continue'
list = ['C', 'Haskell', 'C++', 'Java', 'C#', 'ML', 'Erlang', 'F#']
func_list = ['Haskell', 'ML', 'Erlang', 'F#']

for i in list:
      if i in func_list:
            print 'Found a pure functional language...', i
            continue
else:
      print 'Search complete.'

# for-loop with 'pass'
list = ['C', 'Haskell', 'C++', 'Java', 'C#', 'ML', 'Erlang', 'F#']
func_list = ['Haskell', 'ML', 'Erlang', 'F#']

for i in list:
      if i in func_list:
            pass # do nothing
else:
      print 'Truly time pass...'
