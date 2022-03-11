our_set = {'add'}
print(our_set)

our_set2 = set()
our_set2.add('school')
print(our_set2)

our_set3 = our_set2.union(our_set)
print(our_set3)

print('')
print('вещи на остров')
things1 = set()
things1.add('еда')
things1.add('вода')
things1.add('телефон')
things1.add('спички')
things1.add('fire')
things1.add('walker-19')
things1.add('книжка')
things1.add('очистка воды')
things1.add('палатка')
things1.add('лодка')
print(things1)

things2 = set()
things2.add('еда')
things2.add('леска и крючки')
things2.add('компас')
things2.add('топорик')
things2.add('спички')
print(things2)

print('')
print(things1.union(things2))

print(things1.difference(things2))
