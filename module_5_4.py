class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return 'Ошибка! Введите кол - во этажей'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return 'Ошибка! Введите кол - во этажей'


    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.__add__(value)
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self


    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории ")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# __str__
# print(h1)
# print(h2)

# __eq__
# print(h1 == h2)

# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)

# h1 += 10 # __iadd__
# print(h1)

# h2 = 10 + h2 # __radd__
# print(h2)

# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

# __len__
# print(len(h1))
# print(len(h2))

# Вызовите метод go_to у этого объекта с произвольным числом.
# h1.go_to(5)
# h2.go_to(10)
