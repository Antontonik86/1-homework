immutable_var = tuple([1, 2, 3, True, 'String'])
print(immutable_var)
# immutable_var[3]= 35 кортеж не поддерживает обращение по элементам.
imutable_list = [1, 2, 3, True, 'String']
print(imutable_list)
imutable_list.append('Modified')
print(imutable_list)
print('String' in imutable_list)
imutable_list.remove(2)
print(imutable_list)


