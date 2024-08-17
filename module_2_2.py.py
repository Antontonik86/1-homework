first = int(input('Введите первое число:'))
second = int(input('введите второе число:'))
third = int(input('ведите третье число:'))
if first == second and first == third and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
