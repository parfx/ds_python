# *** Основы объектно-ориентированного программирования (ООП) ***

# Объекты обладают свойствами и методами
# Каждый объект должен принадлежать определенному классу (типу)
# Класс - это "чертеж" объекта
# конкретный реализованный на базе класса объект называется экземпляром класса


# создание класса. Название принято писать с заглавной буквы
class Cat:
	# метод-конструктор
	def __init__(self):
		# свойства (атрибуты, поля)
		self.name = None

	# метод - функция, принадлежащая классу
	def mur(self):
		return self.name

# создание объекта на базе класса Cat (т.е. экземпляра класса Cat)
cat_1 = Cat()

# чтение свойства
var = cat_1.name
# print("Значение var ДО изменения: ", var)

# запись в свойство
cat_1.name = 100
# print(cat_1.name)
# print("Значение var ПОСЛЕ изменения: ", var)

# var = 10
# print(cat_1.name)

# вызов метода экземпляра
res = cat_1.mur()
# print("Результат: ", res)

# каждый объект (экземпляр класса) независим
# создание 2-го экземпляра класса Cat
cat_2 = Cat()
cat_2.name = 200

# вызов метода обеих объектов
# print(cat_1.mur())
# print(cat_2.mur())


# *** Принцип Наследования - принцип ООП ***

# создание родительского (предкового) класса
class Animal:
	def __init__(self):
		self.num_legs = 0

# создание дочерних классов
class Dog(Animal):
	def __init__(self, name):
		self.name = name

	def info(self):
		print(f"My name is {self.name}. Legs: {self.num_legs}")
	
class Insect(Animal):
	"""
	docstring
	"""
	def __init__(self, name):
		self.name = name

	def info(self):
		print(f"My name is {self.name}. Legs: {self.num_legs}")

# создание экземпляров дочерних классов
dog_1 = Dog("Мурзик")
dog_1.num_legs = 4

bug = Insect('Bug')
bug.num_legs = 8

# вызов метода дочерних классов
# dog_1.info()
# bug.info()

class Human(object):
	"""
	docstring
	"""
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def info(self):
		print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")

class Pilot(Human):
	def skill(self):
		print("я умею летать")

class Medic(Human):
	def skill(self):
		print("я умею лечить")

	def therapy(self, obj):
		print(f"Я вылечил {obj.name}")

class Simple_human(Human):
	pass

john = Pilot("John", 45, 82.4)
katrin = Medic("Katrin", 35, 67.5)
petya = Simple_human("Petya", 5, 23.1)

# вызов метода общего для всех (метод наследуется от родительского класса)
john.info()
katrin.info()
petya.info()

# вызов метода, которым обладают все классы, кроме класса Simple_human
john.skill()
katrin.skill()

# вызов метода, которым обладает только класс Medic
katrin.therapy(john)

# try:
# 	petya.skill()
# except AttributeError:
# 	print("у него нету метода skill")
# 	petya.info()