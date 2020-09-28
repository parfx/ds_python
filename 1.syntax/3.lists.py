# Списки (lists)

# Создание пустого списока


my_list = []

my_list_2 = list()

my_list_2.append(3) 
my_list_2.append(1337) 
my_list_2.append(400) 

my_list_2.append("hello")

my_list_2.append([1,2,3])

# обращение к элементам списка

el = my_list_2[0] # извлечение значения по индексу 

# del my_list_2[1] # удаление элемента по индексу

my_list_2[1] = 4040 # замена значения 

# создание заполненого списка

my_list = [10, 20, 30, 40,"A","B"]

s = "йиэээээээээээээс!"

my_list_3 = list(s)

# range(end), создается набор чисел от start до числа end (не включительно)
# range(end, start), создается набор чисел от start до числа end (не включительно)
# range(end, start, step), создается набор чисел от start до числа end (не включительно) с шагом step

numbers = list(range(5))
numbers = list(range(1, 5))
numbers = list(range(1, 5, 10))
numbers = list(range(10, 1, -1))

# *** методы списка ***


a = [100, 200, 300, 400]

# append - метод добавления элемента

# объект, метод()
a.append(100)

# insert - добавляет элемент по индексу
a.insert(0, 7)


# remove - удаляет элемент по значению


# clear - очистка списка 
#print(a)
#a.clear()

# sort - сортировка списка
b = [8,2,1,7,3,2,8,4,1]
b.sort(reverse=True)

# reverse

c = [1,2,3]
c.reverse()

#pop()
#count()
#index()

print(c)