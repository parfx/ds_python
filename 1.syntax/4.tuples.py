# Кортежи (tuples)

#inmutable (неизменяемый) тип коллекций 

my_tuple = (10, 20, 30)

# Чтение данных из кортехи 
num = my_tuple[0]

# нельзя удалить значения 
# del my_tuple[1]

# нельзя менять значения 
# my_tuple[0] = 100


# длина кортежи
# print( len(my_tuple) )

# методы 
# метод count(x) возвращает кол-во элементов со значением x
count = my_tuple.count(20)

# метод Index(x) возвращает индекс элемента со значением x 
idx = my_tuple.index(20)

print(idx)