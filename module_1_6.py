my_dict = {'Anton': 1986, 'Max': 1982, "Ivan": 1980}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Den'))
my_dict.update({'Serg': 1987,
                'Vlad': 1997})
print(my_dict)
del my_dict['Vlad']
print(my_dict)

my_set = {12, 25, 35, 45, 50, 4.31, 35, 52, 531, 'String', True, (12, 22, 32)}
print(my_set)
my_set.add(6)
my_set.add('Hi')
print(my_set)
my_set.pop((12, 22, 32))
print(my_set)
print('Modified set:', my_set)
